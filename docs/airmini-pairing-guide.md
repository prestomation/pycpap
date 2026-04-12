# AirMini BLE Pairing — Implementation Guide

## Goal

Derive the **masterPairKey** from a ResMed AirMini CPAP machine via Bluetooth, so we can authenticate and pull 365 days of therapy data into Home Assistant without the official app.

Once we have masterPairKey, we can:
1. Authenticate via `RequestSession` → `CheckSessionIntegrity` (HMAC-SHA256)
2. Decrypt AES/CBC/NoPadding frames using `session_key = SHA256(SRP_premaster_S).hex()`
3. Pull `GetLoggedData` therapy sessions over BLE
4. Build a Home Assistant integration (like pycpap/ha-cpap-local but for AirMini)

## The Problem

The AirMini uses SRP-6a for first-time pairing. We've fully reverse-engineered the protocol, but extracting masterPairKey from an existing paired phone is blocked:

- **Samsung Knox blocks Frida** (SELinux enforcing, app not debuggable)
- **`adb backup` returns empty** (app has allowBackup=false)
- **No root on Fold 6** to read `/data/data/com.resmed.airmini/`
- **Samsung btsnoop truncates** large ACL packets, so serverPk can't be fully captured

## The Solution: Act as the Bluetooth Server

The AirMini is an SPP **client only** — it dials out to the phone. If we publish an SPP (Serial Port Profile) SDP record on macOS, the AirMini will connect to us instead. Then we perform the SRP-6a exchange as the **server**, generating our own ephemeral private key `b`, computing `S` directly, and deriving masterPairKey.

This requires a macOS app with Bluetooth entitlements.

## Protocol: NCP Frame Format

All communication uses NCP (Network Control Protocol) frames over RFCOMM:

```
[2B unknown/seq] [4B magic: BE BAFECA] [1B direction] [1B version=0x03]
[2B payload_len LE] [8B nonce] [JSON payload] [1B trailer]
```

| Direction byte | Meaning |
|---|---|
| `0x93` | Plain send (phone → device) |
| `0x92` | Plain recv (device → phone) |
| `0x97` | Encrypted send |
| `0x96` | Encrypted recv |

- Encryption bit = bit 2 of direction byte
- Trailer: `0x89` for host→device, `0x53` for device→host (likely CRC8)
- Payload length is exact byte count of JSON payload (little-endian)

## Auth Flow: First-Time Pairing (GetPairKey)

```
Phone (us)                                    AirMini
   |                                              |
   |--- GetVersion (plain) ---------------------->|
   |<-- {device UUID, firmware IDs} --------------|
   |                                              |
   |--- StartKeyExchange {clientPk: A} ---------->|  (A = g^a mod N)
   |<-- {serverPk: B, salt: s} -------------------|  (B = k*v + g^b mod N)
   |                                              |
   |--- ConfirmKeyExchange {clientConfirmation: M1} --->|
   |<-- {serverConfirmation: M2, masterPairKey} --------|  ← THIS IS THE PRIZE
   |                                              |
```

## Auth Flow: Reconnection (GetSessionKey)

```
Phone                                         AirMini
   |                                              |
   |--- GetVersion (plain) ---------------------->|
   |<-- {device UUID, firmware} ------------------|
   |                                              |
   |--- GenerateAuthCode {token, keyLocation:104} ->|
   |<-- {authCode} -------------------------------|
   |                                              |
   |--- RequestSession {} ----------------------->|
   |<-- {challenge, nonce} -----------------------|
   |                                              |
   |--- CheckSessionIntegrity {response} -------->|
   |   response = HMAC-SHA256(masterPairKey, challenge)  |
   |<-- {confirmation: true} ---------------------|
   |                                              |
   |  All subsequent frames: AES/CBC/NoPadding    |
   |  Key = hex-decode(SHA256(premaster_S).hex())|
```

## SRP-6a Cryptographic Parameters (CONFIRMED)

```python
N_hex = "AE2BB17B381BB60C9B8ED2920DBED5E5B7EFDC7C21DFDB0BD4D2D38642E2D4F1F8B3DD686E83DA1FCD16BE815B26B9F6E177B06F7747B718E65A0888706A0FFFCA3B06665C0B0111FF9E658F69AE62F8D3FF6B6145CF6C1678E20AA0EED20DD75483044EC2B30339612667A7F71660D04D476949DB776E3E4A6AD1AEDC5AD6D9"
g = 2
```

- **N**: 1024-bit prime, extracted from `libfiglib.so` `.rodata` at offset `0xcb7f8`
- **g**: 2 (standard SRP generator)
- **Identity string I**: `''` (empty string — confirmed by testing)
- **PIN**: 4-digit number shown on AirMini display during pairing
- **Session key derivation**: `session_key = SHA256(S).hex()` where S is the SRP premaster secret

### SRP-6a Math (Server Side — What We Implement)

```python
import hashlib, secrets

N = int(N_hex, 16)
g = 2
N_BYTES = 128  # 1024 bits

def H(*args):
    """SHA256 hash of concatenated big-endian 128-byte integers"""
    h = hashlib.sha256()
    for a in args:
        if isinstance(a, int): a = a.to_bytes(N_BYTES, 'big')
        elif isinstance(a, str): a = a.encode()
        h.update(a)
    return int.from_bytes(h.digest(), 'big')

def H_bytes(*args):
    """Same as H but returns raw bytes"""
    h = hashlib.sha256()
    for a in args:
        if isinstance(a, int): a = a.to_bytes(N_BYTES, 'big')
        elif isinstance(a, str): a = a.encode()
        h.update(a)
    return h.digest()

# Server-side (we act as server):
PIN = input("Enter PIN from AirMini display: ")  # e.g. "4372"
salt = secrets.token_bytes(32)  # We choose the salt
b = secrets.randbelow(N - 2) + 2  # Our ephemeral private key

# Identity is empty string
x_inner = hashlib.sha256((':' + PIN).encode()).digest()  # H(':' + PIN)
x = int.from_bytes(hashlib.sha256(salt + x_inner).digest(), 'big')
v = pow(g, x, N)  # Verifier

k = H(N, g)  # SRP multiplier
B = (k * v + pow(g, b, N)) % N  # Our public key

# After receiving client's A:
# u = H(A, B)
# S = pow(A * pow(v, u, N), b, N)  # Premaster secret
# session_key = hashlib.sha256(S.to_bytes(N_BYTES, 'big')).hexdigest()
# masterPairKey = session_key  (stored for future reconnections)

# Verify client's M1:
# M1_expected = H_bytes(HNg, HI, salt, A, B, S)
# M2 = H_bytes(A, M1_expected, S)  # Send this back
```

**IMPORTANT**: The identity string for M1 computation is empty (`''`), meaning `H(I) = H(b'')`. This was confirmed by round-trip testing with known values.

## Device Info

- **BT MAC**: `04:87:27:BD:94:7D`
- **RFCOMM Channel**: 6 (iAP profile, `ff 55` framing for inbound)
- **Device UUID**: `11d323cb-7bf4-47f2-a9ef-c6de359ff71b`
- **Firmware**: `SW03900.01.4.0.3.50927`
- **AirMini is SPP client only** — it dials out, won't accept inbound RFCOMM

## Bluetooth Setup on macOS

The AirMini connects as an SPP client. On macOS we need to:

1. **Publish an SPP SDP record** (Serial Port Profile) so the AirMini can discover us
2. **Accept incoming RFCOMM connection** on the published channel
3. **Bridge the RFCOMM data to a Unix socket** (`/tmp/airmini_bridge.sock`) where a Python script handles the NCP/SRP protocol

### macOS Requirements
- macOS needs Bluetooth entitlement (`com.apple.security.device.bluetooth`)
- The Swift binary must be code-signed with this entitlement
- macOS 14+ restricts SPP server publishing — may require `IOBluetoothSDPServiceRecord.publishedServiceRecord(withDictionary:)` or lower-level APIs

### Build Commands
```bash
swiftc -o spp_bridge spp_bridge.swift -framework IOBluetooth -framework AppKit
codesign --force --sign - --entitlements bt.entitlements spp_bridge
```

### Previous Attempt Notes (from 2026-03-26)
- IOBluetooth incoming RFCOMM notification registered but AirMini never connected within 120s timeout
- `IOBluetoothSDPServiceRecord.publishedServiceRecord(withDictionary:)` returned `nil` — macOS may require entitlements
- **Alternative**: Use `IOBluetoothRFCOMMChannel.register(forChannelOpenNotifications:)` with channel 0 (any)
- AirMini was confirmed visible from Mac: MAC `04:87:27:BD:94:7D`, RSSI -57, paired at OS level

## Data Types (After Auth)

Once authenticated, the encrypted frames contain JSON-RPC with these data types:

| VCID | Type | Description |
|------|------|-------------|
| 0x0067 | TherapyOneMinutePeriodic | Minute-by-minute pressure/leak/AHI data |
| 0x0100 | RespiratoryEvent | Apnea/hypopnea event markers |
| 0x0001 | TherapyStatusEvent | Mask on/off, therapy start/stop |
| 0x0004 | MachineMetrics | Device serial, model, usage hours |
| 0x0119 | Diagnostic25HzPeriodic | 25Hz high-frequency pressure/flow samples |

AirMini stores **365 days** of therapy data on-device, accessible via BLE without cloud sync.

## Files to Create on Mac

1. **`spp_bridge.swift`** — Publishes SPP SDP record, accepts RFCOMM, bridges to Unix socket
2. **`bt.entitlements`** — macOS Bluetooth entitlement for code signing
3. **`airmini_pair.py`** — Connects to Unix socket, performs SRP-6a exchange, saves masterPairKey

## What Success Looks Like

1. Run `spp_bridge` on Mac
2. Put AirMini in pairing mode (hold power button until PIN shows + BT blinks)
3. AirMini connects to Mac's SPP service
4. `airmini_pair.py` performs GetVersion → StartKeyExchange → ConfirmKeyExchange
5. `masterPairKey` is saved to `~/dev/airmini/airmini_keys.json`
6. Future sessions: use masterPairKey for CheckSessionIntegrity, then pull therapy data

## References

- `airmini-ble-protocol.md` — Full decompiled source file listing and protocol details
- MEMORY.md entries for 2026-03-21, 2026-03-23, 2026-03-26, 2026-04-12 — session logs
- libfiglib.so (arm64) — Native crypto library, was at `/tmp/airmini-arm64/` (lost, needs re-extraction from phone APK)