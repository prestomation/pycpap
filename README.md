# pycpap

An async Python library for fetching and parsing CPAP therapy data from ResMed devices.

**pycpap is a standalone library.** It has no dependency on Home Assistant or any specific application. It can be used in scripts, data analysis pipelines, dashboards, or any Python application. The [ha-cpap-local](https://github.com/prestomation/ha-cpap-local) Home Assistant integration is one consumer of this library — not the other way around.

## Supported Devices

### SD Card (via WiFi adapter or direct mount)
- ResMed AirSense 10 (AutoSet, Elite, For Her, CS PaceWave)
- ResMed AirSense 11 (AutoSet, AutoSet For Her)
- ResMed S9 series (AutoSet, Elite, VPAP, Escape)

### Bluetooth (planned — see [docs/airmini-protocol.md](docs/airmini-protocol.md))
- ResMed AirMini — data fetched directly from the device over Bluetooth Classic SPP. No SD card or WiFi adapter required. The AirMini stores 365 days of therapy data on-device, so data can be pulled retroactively after travel.

## Installation

```bash
pip install pycpap
```

## Quick Start

### Fetch via HTTP (EZ Share WiFi SD Card)

```python
import asyncio
from pycpap import ResMedReader, HttpFetcher

async def main():
    fetcher = HttpFetcher("http://192.168.4.1")
    reader = ResMedReader(fetcher)

    sessions = await reader.get_sessions()
    for session in sessions:
        print(f"{session.date}: AHI={session.ahi:.1f}, "
              f"Usage={session.duration_minutes/60:.1f}h, "
              f"Mode={session.mode}")

    device = await reader.get_device_info()
    print(f"Device: {device.model} (S/N: {device.serial})")

asyncio.run(main())
```

### Fetch from a Locally Mounted SD Card

```python
from pycpap import ResMedReader, LocalFetcher

fetcher = LocalFetcher("/media/username/RESMED_SD")
reader = ResMedReader(fetcher)
sessions = await reader.get_sessions()
```

### Filter by Date

```python
from datetime import date
sessions = await reader.get_sessions(since=date(2024, 1, 1))
```

### Fetch with DATALOG (High-res per-breath data)

```python
from pycpap import FetchScope
reader = ResMedReader(fetcher, scope=FetchScope.LAST_7_DAYS)
sessions = await reader.get_sessions()
```

## Data Model

### `SleepSession`

| Field | Type | Description |
|---|---|---|
| `date` | `date` | Session date |
| `session_start` | `datetime` | Mask-on time |
| `session_end` | `datetime` | Mask-off time |
| `duration_minutes` | `float` | Total usage duration |
| `ahi` | `float` | Apnea-Hypopnea Index (events/hour) |
| `apnea_index` | `float` | Apnea Index |
| `hypopnea_index` | `float` | Hypopnea Index |
| `mask_leak_median` | `float` | Median mask leak (L/min) |
| `mask_leak_95` | `float` | 95th percentile mask leak |
| `pressure_median` | `float` | Median pressure (cmH₂O) |
| `pressure_95` | `float` | 95th percentile pressure |
| `mode` | `str` | Therapy mode (CPAP, APAP, AutoSet, etc.) |
| `respiratory_rate` | `float \| None` | Respiratory rate (ASV/iVAPS only) |
| `tidal_volume` | `float \| None` | Tidal volume (ASV/iVAPS only) |
| `minute_ventilation` | `float \| None` | Minute ventilation (ASV/iVAPS only) |

### `DeviceInfo`

| Field | Type | Description |
|---|---|---|
| `model` | `str` | Device model name |
| `serial` | `str` | Serial number |
| `firmware` | `str` | Firmware version |

## Architecture

pycpap separates **fetching** from **parsing**:

```
CPAPFetcher          CPAPReader
─────────────        ─────────────────
HttpFetcher    →     ResMedReader  →  list[SleepSession]
LocalFetcher   →                  →  DeviceInfo
AirMiniFetcher →     (planned)
(planned, BT)
```

- **Fetchers** copy raw SD card files (or retrieve data over Bluetooth) to a temporary directory
- **Readers** parse the raw files into typed `SleepSession` objects
- **Your app** (or the HA integration) uses the reader directly — no knowledge of the underlying fetch mechanism required

> **WiFi note:** Network routing to reach your EZ Share adapter is out of scope. The library just takes a URL or path. See your adapter's documentation for setup.

## Documentation

- [`docs/airmini-protocol.md`](docs/airmini-protocol.md) — AirMini Bluetooth protocol reverse engineering notes (NCP framing, VCID table, SRP auth, implementation plan)

## Development

```bash
git clone https://github.com/prestomation/pycpap
cd pycpap
pip install -e ".[dev]"
pytest tests/
```

## License

MIT
