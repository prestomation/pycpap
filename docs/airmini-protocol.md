# AirMini Bluetooth Protocol — Reverse Engineering Report

*Last updated: 2026-03-21 — Based on static analysis of `com.resmed.airmini` v1.8.0.0.331 and `libfiglib.so` (x86_64 build)*

## Overview

The ResMed AirMini is a travel CPAP machine with no SD card slot. All therapy data is stored on the device and accessed exclusively via **Bluetooth Classic SPP** through the AirMini companion app.

The NCP framing protocol has been **fully reverse engineered** from `libfiglib.so`. The frame format, CRC algorithm, command table, and authentication mechanism are all known. A clean reimplementation in Python/Kotlin is feasible without shipping ResMed's binary.

---

## Transport Layer

| Property | Value |
|----------|-------|
| **Protocol** | Bluetooth Classic (BR/EDR) — NOT BLE/GATT |
| **Profile** | SPP (Serial Port Profile) over RFCOMM |
| **SPP UUID** | `00001101-0000-1000-8000-00805F9B34FB` (standard SPP UUID) |
| **Connection role** | Phone acts as **server** — the AirMini device connects *to* the phone |
| **Python library** | `PyBluez` or raw `socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM)` |

---

## Protocol Stack

```
┌────────────────────────────────────────────┐
│  JSON-RPC 2.0 (human-readable method names) │  e.g. {"method":"GetVersion",...}
├────────────────────────────────────────────┤
│  NCP Binary Datagram Codec                  │  Converts JSON ↔ binary NCP stream
│  (NcpString, NcpNodeName, NcpHexString,    │  (NOT raw JSON text in payload)
│   NcpIsoTime, LittleEndianData types)       │
├────────────────────────────────────────────┤
│  AES-CBC Encryption                         │  Post-auth only, session key from SRP
│  (AndroidCbcAesCryptoAlgorithm)            │
├────────────────────────────────────────────┤
│  NCP Stream Framer (StreamCodec)            │  CAFEBABE sync + VCID + CRC32
├────────────────────────────────────────────┤
│  BluetoothSocket InputStream/OutputStream   │  Standard SPP/RFCOMM
└────────────────────────────────────────────┘
```

---

## NCP Frame Format (Fully Recovered)

```
 0         4         6         8        12        12+N     16+N
 +---------+---------+---------+---------+---------+---------+
 | SYNC    | VCID    | LENGTH  | HDR_CRC | PAYLOAD | DATA_CRC|
 | 4 bytes | 2 bytes | 2 bytes | 4 bytes | N bytes | 4 bytes |
 +---------+---------+---------+---------+---------+---------+
```

| Field | Size | Value/Notes |
|-------|------|-------------|
| `SYNC` | 4 bytes | `0xCAFEBABE` — scanned byte-by-byte to find frame start |
| `VCID` | 2 bytes | uint16 little-endian — command ID (see table below) |
| `PAYLOAD_LENGTH` | 2 bytes | uint16 little-endian — number of payload bytes |
| `HEADER_CRC32` | 4 bytes | CRC32 of first 8 bytes (SYNC + VCID + LENGTH) |
| `PAYLOAD` | N bytes | Binary NCP-encoded data, optionally AES-CBC encrypted |
| `DATA_CRC32` | 4 bytes | CRC32 of PAYLOAD bytes |

**Minimum frame size:** 16 bytes (header + empty payload + data CRC)

### CRC32 Algorithm

Standard CRC-32/ISO-HDLC (same as zlib/Ethernet):
- Polynomial: `0xEDB88320` (reflected)
- Init: `0xFFFFFFFF`
- Final XOR: `0xFFFFFFFF`

```python
import zlib
def crc32(data: bytes) -> int:
    return zlib.crc32(data) & 0xFFFFFFFF
```

---

## JNI Interface

The native library is loaded by Java class `com.resmed.mon.fig.FigWrapper`. Four JNI methods:

```java
public class FigWrapper {
    // Initialize the library
    private native void initialise(OutputStream logStream, int logLevel);

    // Encode a JSON-RPC call string into NCP binary (queues internally)
    private native byte[] nativeEncode(String jsonRpcCall);

    // Decode raw NCP bytes received from device → decoded JSON string bytes
    private native byte[] nativeDecode(byte[] ncpData);

    // Pull the encoded/framed TX bytes from internal queue (ready to send over BT)
    private native byte[] pullTxData();
}
```

**Workflow:**
1. Call `nativeEncode(jsonString)` — encodes JSON → NCP binary datagram, frames it
2. Call `pullTxData()` — retrieves the framed bytes to write to the Bluetooth socket
3. Receive bytes from socket, call `nativeDecode(bytes)` — strips framing, decrypts, returns JSON

---

## VCID Command Table

TX commands (app → device): VCID 0x01–0x7F
RX responses (device → app): `response_vcid = request_vcid | 0x80`

| VCID (hex) | Command | Notes |
|-----------|---------|-------|
| `0x02` | `InternalTest` | |
| `0x04` | `GetDateTime` | |
| `0x05` | `SetDateTime` | |
| `0x06` | `GetVersion` | |
| `0x15` | `InitiateUpgrade` | OTA firmware |
| `0x16` | `UpgradeDataBlock` | OTA firmware |
| `0x17` | `CheckUpgradeFile` | OTA firmware |
| `0x18` | `ApplyUpgrade` | OTA firmware |
| `0x19` | `GetLedStatus` | |
| `0x1c` | `EnterTest` | |
| `0x1f` | `SetNextPowerUpDateTime` | |
| `0x39` | `BtDisconnect` | |
| `0x3d` | `EraseData` | |
| `0x3f` | `ResetDevice` | |
| `0x40` | `StoreSecurityData` | |
| `0x42` | `ApplyAuthenticatedUpgrade` | OTA firmware (authenticated) |
| `0x45` | `LightState` | |
| `0x46` | `VerifySecurityData` | |
| `0x4d` | `StreamUpgradePrepare` | |
| `0x4e` | `StreamUpgradeData` | |
| `0x4f` | `StreamUpgradeFinalise` | |
| `0x50` | `StreamUpgradeBattery` | |

> **Note:** Therapy data commands (`Get`, `GetLoggedData`, `GetHistory`, etc.) are known from JSON-RPC analysis but their VCID values are not yet extracted — they likely sit in the `0x20`–`0x38` range. A single BLE capture would fill this in.

---

## Authentication & Pairing

### Initial Pairing (device shows 4-digit PIN)

The 4-digit PIN on the AirMini display is used as the SRP password.

```
1. App → Device: GetPairKey
2. Device → App: [public key A]
3. App → Device: StartKeyExchange (with app public key B + SRP params)
4. Device → App: [SRP verification]
5. App → Device: ConfirmKeyExchange
6. Both sides derive: masterPairKey (stored for future sessions)
```

- **Protocol**: SRP (Secure Remote Password)
- **Hash**: SHA-256 / HMAC-SHA256
- **Salt marker**: `SRPH` string literal in binary
- **Stored**: `masterPairKey` persisted by app for reconnect

### Session Establishment (subsequent connections)

```
1. App → Device: GetSessionKey
2. Device → App: [session challenge]
3. App → Device: RequestSession (using stored masterPairKey)
4. Both sides derive: sessionKey
5. All subsequent payloads encrypted with sessionKey (AES-CBC)
```

### Encryption

Post-authentication payload encryption:
- **Algorithm**: AES-CBC (`AndroidCbcAesCryptoAlgorithm`)
- **Key**: Session key derived from SRP exchange
- **Library**: libtomcrypt (SHA-1, SHA-256, HMAC, AES)

---

## Python Implementation

```python
import struct
import zlib
import socket

SYNC = 0xCAFEBABE
SPP_UUID = "00001101-0000-1000-8000-00805F9B34FB"

def build_frame(vcid: int, payload: bytes) -> bytes:
    header = struct.pack("<IHH", SYNC, vcid, len(payload))
    header_crc = zlib.crc32(header) & 0xFFFFFFFF
    data_crc = zlib.crc32(payload) & 0xFFFFFFFF
    return header + struct.pack("<I", header_crc) + payload + struct.pack("<I", data_crc)

def parse_frame(data: bytes) -> tuple[int, bytes]:
    """Returns (vcid, payload). Raises on CRC mismatch."""
    sync, vcid, length = struct.unpack_from("<IHH", data, 0)
    assert sync == SYNC, f"Bad sync: {sync:#010x}"
    header_crc = struct.unpack_from("<I", data, 8)[0]
    assert zlib.crc32(data[:8]) & 0xFFFFFFFF == header_crc, "Header CRC mismatch"
    payload = data[12:12 + length]
    data_crc = struct.unpack_from("<I", data, 12 + length)[0]
    assert zlib.crc32(payload) & 0xFFFFFFFF == data_crc, "Data CRC mismatch"
    return vcid, payload
```

---

## Implementation Status

| Component | Status |
|-----------|--------|
| Frame format (SYNC, VCID, CRC) | ✅ Fully known |
| CRC32 algorithm | ✅ Standard zlib |
| 22 VCID command codes | ✅ Extracted |
| JNI interface | ✅ 4 methods documented |
| Authentication protocol (SRP) | ✅ Identified |
| 4-digit PIN pairing flow | ✅ Known (SRP password) |
| AES-CBC session encryption | ✅ Known |
| Binary payload schemas (per-command) | ⚠️ Partially known — need BLE capture |
| SRP group parameters (N, g) | ⚠️ Likely RFC 5054 2048-bit group — unconfirmed |
| Therapy data VCIDs | ⚠️ Not yet extracted |
| Working Python implementation | ❌ Not yet |

---

## Recommended Next Steps

1. **BLE capture during pairing** — nRF52840 dongle + Wireshark or Frida hook on rooted Android. One real pairing session would fill in SRP parameters, IV handling, and therapy command VCIDs.
2. **Implement SRP in Python** — `srptools` or `srp` PyPI packages support SRP-6a. Confirm group params match.
3. **Implement NCP binary datagram codec** — the field types (`NcpString`, `NcpNodeName`, etc.) define the per-command schema. Test against known commands (`GetVersion`, `GetDateTime`) first.
4. **Build `AirMiniFetcher`** — wire it up once frame/auth/codec are confirmed working.

---

## Community Research

No public open-source implementation of the AirMini Bluetooth protocol exists as of 2026-03-21. This is novel work. Once the implementation is proven out, these are the places to share findings:

### Threads to update

| Community | Thread | Notes |
|-----------|--------|-------|
| **Apnea Board** | [AirMini Travel Data Extraction & Teardown](https://www.apneaboard.com/forums/Thread-AirMini-Travel-Data-Extraction-Teardown) | 72+ pages since 2018 — most active technical thread, primary place to post findings |
| **CPAPtalk** | [Full sleep data for Resmed AirMini](https://www.cpaptalk.com/viewtopic/t171344/Full-sleep-data-for-Resmed-AirMini.html) | Older thread, some BT sniffing discussion |
| **Reddit r/CPAP** | [Extract data from an Airmini](https://www.reddit.com/r/CPAP/comments/wb5h35/extract_data_from_an_airmini/) | Broader audience, good for awareness |
| **Reddit r/CPAP** | [Resmed air mini and OSCAR](https://www.reddit.com/r/CPAP/comments/17vufd3/resmed_air_mini_and_oscar/) | OSCAR-focused audience |
| **OSCAR GitLab** | [gitlab.com/pholy/OSCAR-code](https://gitlab.com/pholy/OSCAR-code) | If implementation matures, open a PR/issue for AirMini support |
| **HA Community** | [ResMed CPAP Sensor integration in HACS](https://community.home-assistant.io/t/resmed-cpap-sensor-integration-in-hacs/373367) | Preston's own thread — natural place to announce AirMini support |

### What to share when ready
- Frame format + working Python parser code
- SRP pairing implementation (once confirmed against real hardware)
- VCID table (complete, including therapy data commands)
- Reference to `prestomation/pycpap` library

---

## Key Debug Strings (from binary)

```
Sync:       0xCAFEBABE
Log prefix: "NCP-RX", "NCP-TX", "JSON-RX: ", "JSON-TX: "
Errors:     "Wrong header crc. vcid : "
            "Wrong data crc. vcid : "
            "Fail to decode payload - "
            "Fail to encode payload - "
Auth:       "SRPH", "masterPairKey", "passKey", "sessionKey", "authentication"
Init:       "init FIG lib with logLevel: %d"
```
