# pycpap

An async Python library for fetching and parsing CPAP therapy data from ResMed SD cards.

Supports ResMed S9, AirSense 10, and AirSense 11 devices. Can fetch data via HTTP (EZ Share WiFi SD card adapters) or directly from a locally mounted SD card.

> **Note:** WiFi adapter configuration and network routing are out of scope for this library. See your adapter's documentation for setup instructions. Popular options include EZ Share WiFi SD card adapters.

## Installation

```bash
pip install pycpap
```

## Quick Start

### Fetch via HTTP (EZ Share WiFi SD Card)

```python
import asyncio
from pycpap import ResMedReader, HttpFetcher, FetchScope

async def main():
    # Point at your EZ Share adapter's IP address
    fetcher = HttpFetcher("http://192.168.4.1")
    reader = ResMedReader(fetcher)

    # Get all sessions from the last 7 days
    sessions = await reader.get_sessions()
    for session in sessions:
        print(f"{session.date}: AHI={session.ahi:.1f}, "
              f"Usage={session.duration_minutes/60:.1f}h, "
              f"Mode={session.mode}")

    # Get device info
    device = await reader.get_device_info()
    print(f"Device: {device.model} (S/N: {device.serial}, FW: {device.firmware})")

asyncio.run(main())
```

### Fetch from a Locally Mounted SD Card

```python
import asyncio
from pycpap import ResMedReader, LocalFetcher

async def main():
    # Path to the mounted SD card root
    fetcher = LocalFetcher("/media/username/RESMED_SD")
    reader = ResMedReader(fetcher)

    sessions = await reader.get_sessions()
    for session in sessions:
        print(f"{session.date}: AHI={session.ahi:.1f}, "
              f"Leak 95th={session.mask_leak_95:.1f} L/min")

asyncio.run(main())
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
| `pressure_median` | `float` | Median pressure (cmH2O) |
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

## Supported Devices

- ResMed AirSense 10 (AutoSet, Elite, For Her, CS PaceWave)
- ResMed AirSense 11 (AutoSet, AutoSet For Her)
- ResMed S9 series (AutoSet, Elite, VPAP, Escape)

## Development

```bash
git clone https://github.com/prestomation/pycpap
cd pycpap
pip install -e ".[dev]"
pytest tests/
```

## License

MIT
