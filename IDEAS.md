# IDEAS.md — pycpap Future Features

## AirMini Bluetooth Support (Future — Research Phase)

The ResMed AirMini is a travel CPAP with no SD card — all data access is via Bluetooth Classic SPP.
Reverse engineering of the AirMini app (`com.resmed.airmini` v1.8) revealed:

### Protocol Stack
- **Transport:** Bluetooth Classic SPP (RFCOMM), UUID `00001101-0000-1000-8000-00805F9B34FB`
- **Role reversal:** Phone acts as **server** — AirMini device connects *to* the phone
- **Application layer:** JSON-RPC 2.0
- **Framing:** Proprietary NCP layer in native `libfiglib.so` (not yet reversed)
- **Encryption:** Optional AES/CBC with 16-byte random IV prepended to packets

### Pairing Flow
The device shows a 4-digit PIN on its display during pairing. Known RPC methods involved:
- `GetPairKey` — likely retrieves a device-side pairing key
- `GetSessionKey` — session-level key exchange
- `GenerateAuthCode` (v1.1) — probably uses the 4-digit display PIN as input

**Implementation note:** The `AirMiniFetcher` will need a `pair(pin: str)` method that takes the 4-digit code shown on the device display and completes the auth handshake. This needs to be tested against a real device to understand the exact flow.

### Available Data (via `GetLoggedData`)
- `UsageEvents-TherapyStatusEvent` — mask on/off events
- `TherapyEvents-RespiratoryEvent` — apnea/hypopnea/central/obstructive events
- `TherapyOneMinutePeriodic-InspiratoryPressure` — 1-min IPAP pressure
- `TherapyOneMinutePeriodic-Leak` — 1-min leak rate
- `Diagnostic25HzPeriodic-BlowerFlow` — high-res 25Hz flow waveform
- `Diagnostic25HzPeriodic-BlowerPressure` — high-res 25Hz pressure waveform

Other RPC methods: `Get`, `Set`, `GetVersion`, `GetDateTime`, `GetHistory`, `EnterTherapy`, `EnterStandby`, `EnterMaskFit`, `SubscribeEvent`, `StartStream`, `EraseData`, `BtDisconnect`, firmware OTA

### What's Blocking Implementation
The `libfiglib.so` native library handles NCP packet framing — the exact byte format between JSON-RPC and the Bluetooth socket. Options to crack it:
1. Ghidra reverse engineering of `libfiglib.so` (extracted from APK `lib/` directory)
2. Live Bluetooth packet sniffing with nRF Sniffer + Wireshark during real sync
3. MITM proxy approach (rooted Android, intercept socket traffic)

**No public implementation exists** — OSCAR doesn't support AirMini, and the Apnea Board community thread (72+ pages since 2018) never produced working code. This would be novel.

### Python Implementation Path
```python
# Target API shape:
fetcher = AirMiniFetcher(device_address="AA:BB:CC:DD:EE:FF")
await fetcher.pair(pin="1234")  # 4-digit code shown on device display
reader = ResMedAirMiniReader(fetcher=fetcher)
sessions = await reader.get_sessions(since=date.today() - timedelta(days=7))
```

Uses `PyBluez` or raw `socket` with `AF_BLUETOOTH`/`BTPROTO_RFCOMM` (not `bleak` — this is Classic BT, not BLE).

---

## Device Support
- **Philips Respironics support** — DreamStation 1/2, System One. Respironics uses a different SD card format (P-Series .001 files + summary .csv). Would require a separate `RespironicsReader`.
- **F&P (Fisher & Paykel) support** — Icon series devices.

## Data Parsing
- **DATALOG high-res parsing** — Per-breath flow, pressure, leak, and snore waveforms stored in DATALOG/YYYYMMDD/*.edf files. Useful for detailed analysis and flow-limitation detection.
- **SpO2/oximeter data** — ResMed stores pulse oximeter data in SAD.edf files when a compatible oximeter is connected. Parse and expose as optional `SleepSession` fields.
- **Flow limitation index** — Derive from DATALOG waveforms when available.
- **Cheyne-Stokes / CSR detection** — Parse from DATALOG for ASV users.

## Performance
- **Async streaming for large DATALOG fetches** — DATALOG directories can be 100+ MB. Streaming yields individual files as they arrive rather than waiting for the full download.
- **Incremental sync** — Track last-fetched date in a local state file to avoid re-downloading old data.

## CLI
- **CLI tool: `pycpap fetch`** — `pycpap fetch --url http://192.168.4.1 --output ./data` — download to a local directory for archival or analysis.
- **CLI tool: `pycpap stats`** — Print recent session summary stats in the terminal.
- **CLI tool: `pycpap export`** — Export sessions to CSV or JSON for use in spreadsheets / Jupyter notebooks.

## Distribution
- **Type stubs** — Ship a `py.typed` marker and ensure all public APIs are fully typed for downstream IDE support.
- **Async context manager support** — `async with ResMedReader(fetcher) as reader:` for resource cleanup.
