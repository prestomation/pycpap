# AirMini Bluetooth Protocol — Research Notes

*Last updated: 2026-03-21 — Based on static analysis of `com.resmed.airmini` v1.8.0.0.331*

## Overview

The ResMed AirMini is a travel CPAP machine with no SD card slot. All therapy data is stored on the device and accessed exclusively via **Bluetooth Classic SPP** through the AirMini companion app. There is no EZ Share or local file access path.

This document summarizes what's been learned from decompiling the AirMini Android app with jadx and from community research.

---

## Transport Layer

| Property | Value |
|----------|-------|
| **Protocol** | Bluetooth Classic (BR/EDR) — NOT BLE/GATT |
| **Profile** | SPP (Serial Port Profile) over RFCOMM |
| **SPP UUID** | `00001101-0000-1000-8000-00805F9B34FB` (standard SPP UUID) |
| **Connection role** | Phone acts as **server** — the AirMini device connects *to* the phone |
| **Python library** | `PyBluez` or raw `socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM)` — not `bleak` (bleak is BLE only) |

---

## Protocol Stack

```
┌─────────────────────────────────────────┐
│         Application: JSON-RPC 2.0       │  ← All commands and responses
├─────────────────────────────────────────┤
│    libfiglib.so — NCP Framing Layer     │  ← Native C++ — proprietary, not yet reversed
│    (packet framing + optional AES/CBC)  │
├─────────────────────────────────────────┤
│    BluetoothSocket InputStream/         │
│    OutputStream (SPP/RFCOMM)            │  ← Standard Android Bluetooth SPP
└─────────────────────────────────────────┘
```

### libfiglib.so
- Native C++ library bundled with the APK at `lib/arm64-v8a/libfiglib.so`
- Handles NCP (Network Control Protocol) packet framing — vcid (virtual channel ID) headers, CRC
- Optional AES/CBC/NoPadding encryption — 16-byte random IV prepended to each packet
- **This is the main unknown.** The JSON-RPC layer is clean and fully documented, but you cannot reach it without understanding the framing format.

---

## Pairing & Authentication

The AirMini shows a **4-digit PIN on its display** during pairing. The app's auth flow uses these RPC methods:

| Method | Version | Purpose |
|--------|---------|---------|
| `GetPairKey` | 1.0 | Retrieve device-side pairing key |
| `GetSessionKey` | 1.0 | Session key exchange |
| `GenerateAuthCode` | 1.1 | Generate auth code — likely takes the 4-digit PIN as input |

The exact sequence and byte format requires live hardware testing or `libfiglib.so` analysis to determine. The `AirMiniFetcher` implementation will need a `pair(pin: str)` method that accepts the 4-digit code displayed on the device.

---

## JSON-RPC API

All commands are JSON-RPC 2.0. Full method list discovered from static analysis:

### Session / Connection
| Method | Version | Description |
|--------|---------|-------------|
| `GetVersion` | 2.0 | Get device firmware/protocol version |
| `GetDateTime` | 1.0 | Get device clock |
| `BtDisconnect` | 1.0 | Graceful Bluetooth disconnect |

### Authentication
| Method | Version | Description |
|--------|---------|-------------|
| `GetPairKey` | 1.0 | Pairing key retrieval |
| `GetSessionKey` | 1.0 | Session key exchange |
| `GenerateAuthCode` | 1.1 | Auth code generation (uses 4-digit PIN) |

### Therapy Control
| Method | Version | Description |
|--------|---------|-------------|
| `EnterTherapy` | 1.0 | Start therapy session |
| `EnterStandby` | 1.0 | Enter standby mode |
| `EnterMaskFit` | 1.0 | Enter mask fit mode |

### Data Access
| Method | Version | Description |
|--------|---------|-------------|
| `Get` | 1.0 | Read a device parameter/setting |
| `Set` | 1.0 | Write a device parameter/setting |
| `GetLoggedData` | 1.0 | Retrieve therapy history — **primary data method** |
| `GetHistory` | 1.0 | Session history summary |
| `SubscribeEvent` | 1.0 | Subscribe to real-time events |
| `StartStream` | 1.0 | Start high-res data stream |
| `EraseData` | 1.0 | Erase stored therapy data |

### Firmware
OTA firmware update methods (names not fully determined from static analysis)

---

## Available Therapy Data (`GetLoggedData`)

| Data Type Key | Description | Resolution |
|---------------|-------------|-----------|
| `UsageEvents-TherapyStatusEvent` | Mask on/off events | Per-event |
| `TherapyEvents-RespiratoryEvent` | Apnea/hypopnea/central/obstructive events | Per-event |
| `TherapyOneMinutePeriodic-InspiratoryPressure` | IPAP pressure | 1-minute |
| `TherapyOneMinutePeriodic-Leak` | Mask leak rate | 1-minute |
| `Diagnostic25HzPeriodic-BlowerFlow` | Flow rate waveform | 25 Hz |
| `Diagnostic25HzPeriodic-BlowerPressure` | Pressure waveform | 25 Hz |

This covers all metrics needed for `SleepSession`: AHI (derived from `TherapyEvents`), usage hours (from `UsageEvents`), leak (from `TherapyOneMinutePeriodic-Leak`), pressure (from `TherapyOneMinutePeriodic-InspiratoryPressure`).

---

## Target Python API Shape

```python
from pycpap.fetchers.airmini import AirMiniFetcher
from pycpap.readers.resmed_airmini import ResMedAirMiniReader
from datetime import date, timedelta

# 1. Create fetcher with device Bluetooth MAC address
fetcher = AirMiniFetcher(device_address="AA:BB:CC:DD:EE:FF")

# 2. Pair — shows 4-digit PIN on device display
await fetcher.pair(pin="1234")

# 3. Read sessions
reader = ResMedAirMiniReader(fetcher=fetcher)
sessions = await reader.get_sessions(since=date.today() - timedelta(days=7))
device_info = await reader.get_device_info()
```

The `AirMiniFetcher` connects via RFCOMM, handles the NCP framing, and exposes the JSON-RPC interface. The `ResMedAirMiniReader` calls `GetLoggedData` with appropriate data type keys and maps the response to `SleepSession` objects — same interface as the SD card reader.

---

## Implementation Status

| Component | Status |
|-----------|--------|
| JSON-RPC method list | ✅ Complete (from APK static analysis) |
| Available data types | ✅ Complete |
| Pairing flow | ⚠️ Partially known — exact sequence TBD |
| NCP framing (libfiglib.so) | ❌ Unknown — main blocker |
| Encryption details | ⚠️ AES/CBC/NoPadding with random IV — key derivation unknown |
| Working Python implementation | ❌ Not yet |

---

## How to Unblock: libfiglib.so

Three approaches to reverse the NCP framing layer:

### Option 1: Ghidra (static)
Extract `libfiglib.so` from the APK:
```bash
unzip com.resmed.airmini.apk lib/arm64-v8a/libfiglib.so -d /tmp/airmini-lib
```
Load into Ghidra, find the `encode`/`decode`/`frame` functions and reverse the byte format. Moderate difficulty — the library isn't obfuscated, just compiled native code.

### Option 2: Live Bluetooth Sniffing (hardware)
Use a **nRF Sniffer for Bluetooth Classic** + Wireshark to capture real packets during an AirMini sync. Compare captured bytes against the JSON-RPC payloads to reverse the framing.

Required hardware: nRF52840 dongle (~$10) + nRF Sniffer firmware

### Option 3: Android MITM Proxy
On a rooted Android device, intercept the `BluetoothSocket` InputStream/OutputStream at the Java layer (Frida hook) before libfiglib touches it. Captures raw unframed JSON-RPC. Easier than reversing the native binary.

---

## Community Research

- **Apnea Board thread** — "AirMini Travel Data Extraction & Teardown" — 72+ pages since 2018. No working implementation published.
- **OSCAR** — Does not support AirMini. The SD card format (used by AirSense 10/11) is completely different.
- **SleepHQ** — Cloud only for AirMini. No local data access.

No public open-source implementation of the AirMini Bluetooth protocol exists as of 2026-03-21. This would be novel work.
