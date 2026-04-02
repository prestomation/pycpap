#!/usr/bin/env python3
"""
AirMini pairing — macOS IOBluetooth SPP server.
pip3 install pyobjc-framework-IOBluetooth
"""

import struct, os, json, time
import objc
from Foundation import NSObject, NSRunLoop, NSDate
import IOBluetooth

MAGIC = bytes([0xBE, 0xBA, 0xFE, 0xCA])

def build_frame(payload: str, direction: int = 0x93) -> bytes:
    p = payload.encode()
    return (b'\x00\x00' + MAGIC +
            bytes([direction, 0x03]) +
            struct.pack('<H', len(p)) +
            os.urandom(8) + p + bytes([0x89]))

def parse_frame(data: bytes) -> str | None:
    pos = data.find(MAGIC)
    if pos < 2: return None
    plen = struct.unpack_from('<H', data, pos + 6)[0]
    return data[pos + 16: pos + 16 + plen].decode('utf-8', errors='replace')

class Session(NSObject):
    def init(self):
        self = objc.super(Session, self).init()
        self.channel = None
        self._buf = b''
        self.ready = False
        return self

    # Called when AirMini opens a channel to us
    def rfcommChannelOpenComplete_status_(self, ch, status):
        print(f"  rfcommChannelOpenComplete status={status:#010x}")
        if status == 0:
            self.channel = ch
            self.ready = True
            dev = ch.getDevice()
            print(f"  Connected: {dev.getName() if dev else 'unknown'} ✓")
        else:
            print(f"  Open failed: {status:#010x}")

    def rfcommChannelData_data_length_(self, ch, data, length):
        self._buf += bytes(objc.varlist(data, length))

    def rfcommChannelClosed_(self, ch):
        print("  Channel closed")

    # Notification callback — incoming connection
    def newChannelNotification_channel_(self, note, ch):
        print(f"  Incoming RFCOMM channel! setting delegate...")
        ch.setDelegate_(self)
        # Open it
        ch.openChannel()

    def ncp_read(self, timeout=8.0):
        self._buf = b''
        deadline = time.time() + timeout
        while time.time() < deadline:
            NSRunLoop.currentRunLoop().runUntilDate_(
                NSDate.dateWithTimeIntervalSinceNow_(0.05))
            if MAGIC in self._buf:
                text = parse_frame(self._buf)
                self._buf = b''
                return text
        return None

    def ncp_write(self, payload: str):
        frame = build_frame(payload)
        self.channel.writeSync_length_(frame, len(frame))

PIN = input("Enter AirMini PIN: ").strip()
session = Session.alloc().init()

# Register for ALL incoming RFCOMM channels (channelID=0 = any)
print("\nRegistering for incoming RFCOMM connections (any channel)...")
note = IOBluetooth.IOBluetoothRFCOMMChannel.registerForChannelOpenNotifications_selector_withChannelID_direction_(
    session,
    "newChannelNotification:channel:",
    0,   # 0 = any channel
    2    # kIOBluetoothUserNotificationChannelDirectionIncoming
)
print(f"  Notification registered: {note}")

# Also check if AirMini already has an open connection
print("\nChecking existing BT connections...")
paired = IOBluetooth.IOBluetoothDevice.pairedDevices()
if paired:
    for dev in paired:
        name = dev.getName() or ""
        if "ResMed" in name or "254298" in name:
            print(f"  Found: {name} — connected={dev.isConnected()}")
            if dev.isConnected():
                # Try opening RFCOMM on any channel
                for ch_id in [1, 2, 3, 4]:
                    print(f"  Trying RFCOMM channel {ch_id}...")
                    status, ch = dev.openRFCOMMChannelSync_withChannelID_delegate_(
                        None, ch_id, session)
                    print(f"    status={status:#010x}")
                    if status == 0 and ch:
                        session.channel = ch
                        session.ready = True
                        print(f"  Opened channel {ch_id} ✓")
                        break

print("\nWaiting for AirMini to connect (60s)...")
print("If not already paired: System Settings → Bluetooth → pair 'ResMed 254298'")
print("Then put AirMini in pairing mode (hold power until PIN shows)\n")

deadline = time.time() + 60
while time.time() < deadline:
    NSRunLoop.currentRunLoop().runUntilDate_(
        NSDate.dateWithTimeIntervalSinceNow_(0.1))
    if session.ready:
        break
else:
    print("Timed out. AirMini did not connect.")
    exit(1)

def rpc(method, params=None, id_=1):
    msg = {"id": id_, "jsonrpc": "2.0", "method": method}
    if params: msg["params"] = params
    print(f"  → {json.dumps(msg)[:120]}")
    session.ncp_write(json.dumps(msg))
    text = session.ncp_read(timeout=8.0)
    if not text:
        print(f"  Timeout on {method}")
        return None
    print(f"  ← {text[:200]}")
    try: return json.loads(text)
    except: return None

print("GetVersion →")
r = rpc("GetVersion", id_=1)
if r and "result" in r:
    fg = r["result"].get("FlowGenerator", {})
    ip = fg.get("IdentificationProfiles", {})
    print(f"  UUID:     {ip.get('Product', {}).get('UniversalIdentifier', '?')}")
    print(f"  Firmware: {ip.get('Software', {}).get('ApplicationIdentifier', '?')}")

print("\nGetPairKey →")
r = rpc("GetPairKey", {"passKey": PIN}, id_=2)
if r and "result" in r:
    res = r["result"]
    mpk, sk, nonce = res.get("masterPairKey"), res.get("sessionKey"), res.get("nonce")
    print(f"\n  ✅ masterPairKey = {mpk}")
    print(f"     sessionKey    = {sk}")
    with open("airmini_keys.json", "w") as f:
        json.dump({"masterPairKey": mpk, "sessionKey": sk, "nonce": nonce}, f, indent=2)
    print("  Saved → airmini_keys.json 🎉")
else:
    print("  ❌ No masterPairKey in response")

if session.channel:
    session.channel.closeChannel()
