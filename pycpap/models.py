from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class DeviceInfo:
    model: str
    serial: str
    firmware: str


@dataclass
class SleepSession:
    date: date
    session_start: datetime
    session_end: datetime
    duration_minutes: float
    ahi: float
    apnea_index: float
    hypopnea_index: float
    mask_leak_median: float
    mask_leak_95: float
    pressure_median: float
    pressure_95: float
    mode: str
    respiratory_rate: float | None = None
    tidal_volume: float | None = None
    minute_ventilation: float | None = None
