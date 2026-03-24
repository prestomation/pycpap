#!/usr/bin/env python3
"""
AirMini pairing test — macOS version using IOBluetooth via pyobjc
"""

import struct, os, json, time, threading
import objc
from Foundation import NSObject, NSRunLoop, NSDate
import IOBluetooth

AIRMINI_MAC = "04:87:27:BD:94:7D"
MAGIC = bytes([0xBE, 0xBA, 0xFE, 0xCA])

# ── NCP framing ──────────────────────────────────────────────────────────────
def build_frame(payload: str, direction: int = 0x93) -> bytes:
    p = payload.encode()
    return (b'\x00\x00' + MAGIC +
            bytes([direction, 0x03]) +
            struct.pack('<H', len(p)) +
            os.urandom(8) +
            p +
            bytes([0x89]))

def parse_frame(data: bytes) -> str | None:
    pos = data.find(MAGIC)
    if pos < 2: return None
    plen = struct.unpack_from('<H', data, pos + 6)[0]
    return data[pos + 16: pos + 16 + plen].decode('utf-8', errors='replace')

# ── IOBluetooth RFCOMM delegate ───────────────────────────────────────────────
class RFCOMMDelegate(NSObject):
    def init(self):
        self = objc.super(RFCOMMDelegate, self).init()
        self._connected = False
        self._data = b''
        self._event = threading.Event()
        return self

    def rfcommChannelOpenComplete_status_(self, channel, status):
        if status == 0:
            self._connected = True
            print("  RFCOMM channel open ✓")
        else:
            print(f"  RFCOMM open failed, status={status}")
        self._event.set()

    def rfcommChannelData_data_length_(self, channel, data, length):
        self._data += bytes(objc.varlist(data, length))
        self._event.set()

    def rfcommChannelClosed_(self, channel):
        print("  Channel closed")

    def wait_for_data(self, timeout=5.0):
        self._event.clear()
        deadline = time.time() + timeout
        while time.time() < deadline:
            NSRunLoop.currentRunLoop().runUntilDate_(
                NSDate.dateWithTimeIntervalSinceNow_(0.05))
            if self._data:
                data = self._data
                self._data = b''
                return data
        return None

# ── Main ──────────────────────────────────────────────────────────────────────
PIN = input("Enter AirMini PIN: ").strip()

print(f"\nLooking up device {AIRMINI_MAC}...")
device = IOBluetooth.IOBluetoothDevice.deviceWithAddressString_(AIRMINI_MAC)
if not device:
    print("Device not found — make sure AirMini is in pairing mode and in range")
    exit(1)

delegate = RFCOMMDelegate.alloc().init()

print("Opening RFCOMM channel 1 (SPP)...")
channel = IOBluetooth.IOBluetoothRFCOMMChannel.alloc().init()
status = device.openRFCOMMChannelSync_withChannelID_delegate_(
    objc.byref(channel), 1, delegate)

if status != 0 or not delegate._connected:
    # Try SDP-discovered channel
    print(f"  Direct channel 1 failed (status={status}), trying SDP lookup...")
    services = device.services()
    rfcomm_channel = None
    if services:
        for svc in services:
            ch = svc.getRFCOMMChannelID()
            if ch > 0:
                rfcomm_channel = ch
                print(f"  Found SPP channel via SDP: {rfcomm_channel}")
                break
    if rfcomm_channel:
        status = device.openRFCOMMChannelSync_withChannelID_delegate_(
            objc.byref(channel), rfcomm_channel, delegate)
    if status != 0:
        print(f"  Failed to open RFCOMM (status={status})")
        exit(1)

# Give it a moment
NSRunLoop.currentRunLoop().runUntilDate_(NSDate.dateWithTimeIntervalSinceNow_(0.5))

def send_rpc(method, params=None, id_=1):
    msg = {"id": id_, "jsonrpc": "2.0", "method": method}
    if params:
        msg["params"] = params
    frame = build_frame(json.dumps(msg))
    channel.writeSync_length_(frame, len(frame))
    data = delegate.wait_for_data(timeout=8.0)
    if not data:
        print(f"  Timeout waiting for {method} response")
        return None
    text = parse_frame(data)
    if text:
        print(f"  ← {text[:200]}")
        try:
            return json.loads(text)
        except:
            return None
    return None

print("\nGetVersion →")
result = send_rpc("GetVersion", id_=1)
if result and "result" in result:
    fg = result["result"].get("FlowGenerator", {})
    ip = fg.get("IdentificationProfiles", {})
    uuid = ip.get("Product", {}).get("UniversalIdentifier", "?")
    sw   = ip.get("Software", {}).get("ApplicationIdentifier", "?")
    print(f"  Device UUID: {uuid}")
    print(f"  Firmware:    {sw}")

print("\nGetPairKey →")
result = send_rpc("GetPairKey", {"passKey": PIN}, id_=2)
if result and "result" in result:
    r = result["result"]
    mpk = r.get("masterPairKey")
    sk  = r.get("sessionKey")
    nonce = r.get("nonce")
    print(f"\n  ✅ masterPairKey  = {mpk}")
    print(f"     sessionKey     = {sk}")
    print(f"     nonce          = {nonce}")
    with open("airmini_keys.json", "w") as f:
        json.dump({"mac": AIRMINI_MAC, "masterPairKey": mpk,
                   "sessionKey": sk, "nonce": nonce}, f, indent=2)
    print("\n  Saved → airmini_keys.json 🎉")
else:
    print("  ❌ No masterPairKey in response")

channel.closeChannel()
