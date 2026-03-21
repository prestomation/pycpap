# IDEAS.md — pycpap Future Features

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
