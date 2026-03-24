#!/usr/bin/env python3
"""
AirMini pairing — macOS, using IOBluetooth RFCOMM server.
No extra packages needed beyond pyobjc (ships with macOS Python).

Install deps:  pip3 install pyobjc-framework-IOBluetooth
"""

import struct, os, json, time
import objc
from Foundation import NSObject, NSRunLoop, NSDate
import IOBluetooth

MAGIC = bytes([0xBE, 0xBA, 0xFE, 0xCA])

# ── NCP framing ──────────────────────────────────────────────────────────────
def build_frame(payload: str, direction: int = 0x93) -> bytes:
    p = payload.encode()
    return (b'\x00\x00' + MAGIC +
            bytes([direction, 0x03]) +
            struct.pack('<H', len(p)) +
            os.urandom(8) + p +
            bytes([0x89]))

def parse_frame(data: bytes) -> str | None:
    pos = data.find(MAGIC)
    if pos < 2: return None
    plen = struct.unpack_from('<H', data, pos + 6)[0]
    return data[pos + 16: pos + 16 + plen].decode('utf-8', errors='replace')

# ── Delegate: handles the connected channel ───────────────────────────────────
class ChannelDelegate(NSObject):
    def init(self):
        self = objc.super(ChannelDelegate, self).init()
        self.channel = None
        self._buf = b''
        self._ready = False
        return self

    def rfcommChannelOpenComplete_status_(self, ch, status):
        if status == 0:
            self.channel = ch
            self._ready = True
            dev = ch.getDevice()
            print(f"  AirMini connected: {dev.getName()} ✓")
        else:
            print(f"  Channel open failed: {status:#010x}")

    def rfcommChannelData_data_length_(self, ch, data, length):
        self._buf += bytes(objc.varlist(data, length))

    def rfcommChannelClosed_(self, ch):
        print("  Channel closed")

    def recv(self, timeout=8.0):
        deadline = time.time() + timeout
        self._buf = b''
        while time.time() < deadline:
            NSRunLoop.currentRunLoop().runUntilDate_(
                NSDate.dateWithTimeIntervalSinceNow_(0.05))
            if MAGIC in self._buf:
                text = parse_frame(self._buf)
                self._buf = b''
                return text
        return None

    def send_frame(self, payload: str):
        frame = build_frame(payload)
        self.channel.writeSync_length_(frame, len(frame))

# ── Notification handler: fires when AirMini opens a channel ──────────────────
_delegate = None  # keep alive

class NotificationHandler(NSObject):
    def rfcommChannelNotification_channel_(self, note, channel):
        global _delegate
        print(f"  Incoming RFCOMM connection!")
        channel.setDelegate_(_delegate)
        _delegate.channel = channel
        _delegate._ready = True
        dev = channel.getDevice()
        print(f"  Device: {dev.getName() if dev else 'unknown'} ✓")

# ── Main ──────────────────────────────────────────────────────────────────────
PIN = input("Enter AirMini PIN: ").strip()

_delegate = ChannelDelegate.alloc().init()
handler   = NotificationHandler.alloc().init()

# Register to receive notifications for any incoming RFCOMM channel on ch 1
# kIOBluetoothUserNotificationChannelDirectionIncoming = 2
note = IOBluetooth.IOBluetoothRFCOMMChannel.registerForChannelOpenNotifications_selector_withChannelID_direction_(
    handler,
    "rfcommChannelNotification:channel:",
    1,    # channel ID (SPP)
    2     # incoming direction
)

print("\nWaiting for AirMini to connect (up to 60s)...")
print("→ Put AirMini in pairing mode: hold power button until PIN shows on screen")
print("→ On your Mac: System Settings → Bluetooth → pair with 'ResMed 254298'\n")

deadline = time.time() + 60
while time.time() < deadline:
    NSRunLoop.currentRunLoop().runUntilDate_(
        NSDate.dateWithTimeIntervalSinceNow_(0.1))
    if _delegate._ready:
        break
else:
    print("Timed out — AirMini did not connect.")
    print("Make sure:")
    print("  1. AirMini is in pairing mode (PIN visible on its display)")
    print("  2. Mac's Bluetooth is ON")
    print("  3. 'ResMed 254298' is paired in System Settings → Bluetooth")
    exit(1)

def rpc(method, params=None, id_=1):
    msg = {"id": id_, "jsonrpc": "2.0", "method": method}
    if params:
        msg["params"] = params
    _delegate.send_frame(json.dumps(msg))
    text = _delegate.recv(timeout=8.0)
    if not text:
        print(f"  Timeout waiting for {method}")
        return None
    print(f"  ← {text[:200]}")
    try:
        return json.loads(text)
    except:
        return None

print("\nGetVersion →")
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
    mpk   = res.get("masterPairKey")
    sk    = res.get("sessionKey")
    nonce = res.get("nonce")
    print(f"\n  ✅ masterPairKey = {mpk}")
    print(f"     sessionKey    = {sk}")
    print(f"     nonce         = {nonce}")
    with open("airmini_keys.json", "w") as f:
        json.dump({"masterPairKey": mpk, "sessionKey": sk, "nonce": nonce}, f, indent=2)
    print("\n  Saved → airmini_keys.json 🎉")
else:
    print("  ❌ No masterPairKey in response")

if _delegate.channel:
    _delegate.channel.closeChannel()
