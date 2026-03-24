#!/usr/bin/env python3
"""
AirMini pairing — macOS, using lightblue for SPP server.

Install: pip3 install lightblue
NOTE: lightblue requires Bluetooth permission for Terminal in
      System Settings → Privacy & Security → Bluetooth
"""

import json, struct, os, threading

try:
    import lightblue
except ImportError:
    print("Install lightblue first: pip3 install lightblue")
    exit(1)

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

def send_rpc(sock, method, params=None, id_=1):
    msg = {"id": id_, "jsonrpc": "2.0", "method": method}
    if params:
        msg["params"] = params
    sock.send(build_frame(json.dumps(msg)))
    raw = b''
    sock.settimeout(8.0)
    try:
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            raw += chunk
            if MAGIC in raw:
                text = parse_frame(raw)
                if text:
                    print(f"  ← {text[:200]}")
                    try:
                        return json.loads(text)
                    except:
                        return None
    except Exception as e:
        print(f"  recv timeout/error: {e}")
    return None

# ── Main ──────────────────────────────────────────────────────────────────────
PIN = input("Enter AirMini PIN: ").strip()

print("\nStarting SPP server (channel 1)...")
print("Put AirMini in pairing mode (hold power until PIN shows on display).")
print("Waiting for AirMini to connect to your Mac...\n")

# lightblue acts as SPP server — AirMini connects to us
server_sock = lightblue.socket(lightblue.RFCOMM)
server_sock.bind(("", 0))
server_sock.listen(1)

# Advertise the SPP service
lightblue.advertise("BluetoothConnection", server_sock, lightblue.RFCOMM)

print(f"Listening on channel {server_sock.getsockname()[1]}...")
conn, addr = server_sock.accept()
print(f"  ← Connected from {addr} ✓\n")

print("GetVersion →")
result = send_rpc(conn, "GetVersion", id_=1)
if result and "result" in result:
    fg = result["result"].get("FlowGenerator", {})
    ip = fg.get("IdentificationProfiles", {})
    uuid = ip.get("Product", {}).get("UniversalIdentifier", "?")
    sw   = ip.get("Software", {}).get("ApplicationIdentifier", "?")
    print(f"  Device UUID: {uuid}")
    print(f"  Firmware:    {sw}")

print("\nGetPairKey →")
result = send_rpc(conn, "GetPairKey", {"passKey": PIN}, id_=2)
if result and "result" in result:
    r = result["result"]
    mpk   = r.get("masterPairKey")
    sk    = r.get("sessionKey")
    nonce = r.get("nonce")
    print(f"\n  ✅ masterPairKey  = {mpk}")
    print(f"     sessionKey     = {sk}")
    print(f"     nonce          = {nonce}")
    with open("airmini_keys.json", "w") as f:
        json.dump({"masterPairKey": mpk, "sessionKey": sk, "nonce": nonce}, f, indent=2)
    print("\n  Saved → airmini_keys.json 🎉")
else:
    print("  ❌ No masterPairKey in response")

conn.close()
server_sock.close()
