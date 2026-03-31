"""ResMedReader — parses ResMed SD card data (STR.edf + identification.txt).

Supports ResMed S9, AirSense 10, and AirSense 11 devices.
"""

import asyncio
import re
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path

import pyedflib
import numpy as np

from ..fetchers.base import CPAPFetcher, FetchScope
from ..models import DeviceInfo, SleepSession
from .base import CPAPReader

# Signal name mappings for different ResMed device generations.
# Key = canonical name, Value = list of signal name variants to try (in order).
_SIGNAL_MAP: dict[str, list[str]] = {
    "MaskOn": ["MaskOn"],
    "MaskOff": ["MaskOff"],
    "AHI": ["AHI", "AHI.Calc"],
    "AI": ["AI", "OAI"],
    "HI": ["HI"],
    "Leak": ["Leak", "LeakMed", "Lk"],
    "Leak95": ["Leak.95", "Lk95"],
    "MaskPres": ["MaskPres", "Pres", "Pressure"],
    "MaskPres95": ["MaskPres.95", "Pres95"],
    "Duration": ["Duration", "Dur"],
    # AirSense 11 / ASV optional signals
    "RespRate": ["RespRate", "RR"],
    "TidalVolume": ["Tidal", "TV"],
    "MinVent": ["MinVent", "MV"],
    # S9 therapy mode
    "Mode": ["Mode", "TherapyMode"],
}


def _find_signal(
    signal_labels: list[str], candidates: list[str]
) -> int | None:
    """Return the index of the first matching signal label, or None."""
    labels_upper = [s.upper() for s in signal_labels]
    for candidate in candidates:
        try:
            return labels_upper.index(candidate.upper())
        except ValueError:
            continue
    return None


def _read_signal(f: pyedflib.EdfReader, idx: int) -> np.ndarray:
    return f.readSignal(idx)


class ResMedReader(CPAPReader):
    """Parses ResMed CPAP therapy data from STR.edf and identification.txt.

    Supports fetching via a CPAPFetcher (network/mount) or parsing from raw
    bytes already in memory (useful when data was fetched by an external agent).

    Args:
        fetcher: A CPAPFetcher instance used to download/copy SD card files.
        scope: FetchScope to use when calling fetcher.fetch().
    """

    def __init__(self, fetcher: CPAPFetcher, scope: FetchScope = FetchScope.SUMMARY_ONLY) -> None:
        self.fetcher = fetcher
        self.scope = scope

    @classmethod
    def from_bytes(
        cls,
        edf_data: bytes,
        identification_data: bytes | None = None,
        since: date | None = None,
    ) -> tuple[list[SleepSession], DeviceInfo | None]:
        """Parse EDF bytes directly without a fetcher.

        Use this when an external agent (e.g. an ESP32 WiFi bridge) has already
        downloaded the EDF file and delivered the raw bytes via HTTP POST.

        Args:
            edf_data: Raw bytes of the STR.EDF file.
            identification_data: Raw bytes of the IDENTIFICATION.TXT file
                (optional; primarily used for device info when fetcher is absent).
            since: Only return sessions on or after this date (optional).

        Returns:
            A tuple of (list of SleepSession, DeviceInfo). DeviceInfo may be
            None if identification_data is not provided.

        Raises:
            ValueError: If edf_data is empty or not a valid EDF file.
        """
        if not edf_data:
            raise ValueError("edf_data must be non-empty bytes")

        tmp = Path(tempfile.mkdtemp(prefix="pycpap_bytes_"))
        try:
            edf_path = tmp / "STR.EDF"
            edf_path.write_bytes(edf_data)

            id_path = tmp / "IDENTIFICATION.TXT"
            if identification_data:
                id_path.write_bytes(identification_data)

            # Build a minimal reader instance to call the sync parsers
            class _NoOpFetcher(CPAPFetcher):
                async def fetch(self, dest_dir, since=None, scope=FetchScope.SUMMARY_ONLY):
                    pass

            reader = cls(_NoOpFetcher())
            try:
                sessions = reader._parse_str_edf(tmp, since)
            except OSError as exc:
                raise ValueError(f"edf_data is not a valid EDF file: {exc}") from exc
            try:
                device_info = reader._parse_identification(tmp) if identification_data else None
            except FileNotFoundError:
                device_info = None
            return sessions, device_info
        finally:
            import shutil
            shutil.rmtree(tmp, ignore_errors=True)

    async def _fetch_to_temp(self) -> Path:
        """Fetch SD card files to a temporary directory and return its path."""
        tmp = Path(tempfile.mkdtemp(prefix="pycpap_"))
        await self.fetcher.fetch(tmp, scope=self.scope)
        return tmp

    async def get_sessions(self, since: date | None = None) -> list[SleepSession]:
        """Parse STR.edf and return a list of SleepSessions."""
        tmp_dir = await self._fetch_to_temp()
        try:
            return await asyncio.get_event_loop().run_in_executor(
                None, self._parse_str_edf, tmp_dir, since
            )
        finally:
            import shutil
            shutil.rmtree(tmp_dir, ignore_errors=True)

    async def get_device_info(self) -> DeviceInfo:
        """Parse identification.txt and return DeviceInfo."""
        tmp_dir = await self._fetch_to_temp()
        try:
            return await asyncio.get_event_loop().run_in_executor(
                None, self._parse_identification, tmp_dir
            )
        finally:
            import shutil
            shutil.rmtree(tmp_dir, ignore_errors=True)

    def _parse_str_edf(self, data_dir: Path, since: date | None) -> list[SleepSession]:
        """Synchronous EDF parsing — runs in executor to avoid blocking event loop."""
        edf_path = data_dir / "STR.EDF"
        if not edf_path.exists():
            raise FileNotFoundError(f"STR.EDF not found in {data_dir}")

        sessions: list[SleepSession] = []

        with pyedflib.EdfReader(str(edf_path)) as f:
            labels = f.getSignalLabels()
            n_samples = f.getNSamples()
            start_dt = f.getStartdatetime()

            def get_signal(canonical: str) -> np.ndarray | None:
                idx = _find_signal(labels, _SIGNAL_MAP.get(canonical, [canonical]))
                if idx is None:
                    return None
                return _read_signal(f, idx)

            mask_on = get_signal("MaskOn")
            mask_off = get_signal("MaskOff")
            ahi_sig = get_signal("AHI")
            ai_sig = get_signal("AI")
            hi_sig = get_signal("HI")
            leak_sig = get_signal("Leak")
            leak95_sig = get_signal("Leak95")
            pres_sig = get_signal("MaskPres")
            pres95_sig = get_signal("MaskPres95")
            dur_sig = get_signal("Duration")
            mode_sig = get_signal("Mode")
            rr_sig = get_signal("RespRate")
            tv_sig = get_signal("TidalVolume")
            mv_sig = get_signal("MinVent")

            if mask_on is None or mask_off is None:
                raise ValueError("STR.EDF does not contain MaskOn/MaskOff signals")

            # STR.edf records are typically daily (one record per day)
            # The signal index corresponds to the day offset from start_dt
            n_records = len(mask_on)

            for i in range(n_records):
                # MaskOn / MaskOff values are minutes from midnight
                on_minutes = float(mask_on[i]) if mask_on is not None else 0.0
                off_minutes = float(mask_off[i]) if mask_off is not None else 0.0

                # Skip days with no therapy (MaskOn == 0 typically means no session)
                if on_minutes == 0 and off_minutes == 0:
                    continue

                # Calculate session date
                from datetime import timedelta
                session_date = (start_dt + timedelta(days=i)).date()
                if since is not None and session_date < since:
                    continue

                # Build datetime objects
                midnight = datetime(
                    session_date.year, session_date.month, session_date.day,
                    tzinfo=None,
                )
                session_start = midnight + timedelta(minutes=on_minutes)
                session_end = midnight + timedelta(minutes=off_minutes)

                duration = float(dur_sig[i]) if dur_sig is not None else (off_minutes - on_minutes)

                # Mode mapping (ResMed encodes mode as integer)
                mode_val = int(mode_sig[i]) if mode_sig is not None else 0
                mode_str = _decode_mode(mode_val)

                sessions.append(
                    SleepSession(
                        date=session_date,
                        session_start=session_start,
                        session_end=session_end,
                        duration_minutes=abs(duration),
                        ahi=float(ahi_sig[i]) if ahi_sig is not None else 0.0,
                        apnea_index=float(ai_sig[i]) if ai_sig is not None else 0.0,
                        hypopnea_index=float(hi_sig[i]) if hi_sig is not None else 0.0,
                        mask_leak_median=float(leak_sig[i]) if leak_sig is not None else 0.0,
                        mask_leak_95=float(leak95_sig[i]) if leak95_sig is not None else 0.0,
                        pressure_median=float(pres_sig[i]) if pres_sig is not None else 0.0,
                        pressure_95=float(pres95_sig[i]) if pres95_sig is not None else 0.0,
                        mode=mode_str,
                        respiratory_rate=float(rr_sig[i]) if rr_sig is not None else None,
                        tidal_volume=float(tv_sig[i]) if tv_sig is not None else None,
                        minute_ventilation=float(mv_sig[i]) if mv_sig is not None else None,
                    )
                )

        return sorted(sessions, key=lambda s: s.date)

    def _parse_identification(self, data_dir: Path) -> DeviceInfo:
        """Parse identification.txt for device metadata."""
        id_path = data_dir / "IDENTIFICATION.TXT"
        if not id_path.exists():
            raise FileNotFoundError(f"IDENTIFICATION.TXT not found in {data_dir}")

        fields: dict[str, str] = {}
        with open(id_path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if "=" in line:
                    key, _, value = line.partition("=")
                    fields[key.strip().upper()] = value.strip()

        return DeviceInfo(
            model=fields.get("PRODUCTNAME", fields.get("MODEL", "Unknown")),
            serial=fields.get("SERIALNO", fields.get("SERIAL", "Unknown")),
            firmware=fields.get("SWVERSION", fields.get("FIRMWARE", "Unknown")),
        )


# ResMed therapy mode integer → string mapping
_MODE_MAP: dict[int, str] = {
    0: "Unknown",
    1: "CPAP",
    2: "APAP",
    3: "AutoSet",
    4: "BiLevel",
    5: "ASV",
    6: "iVAPS",
    7: "ST",
    8: "CPAP-Check",
    9: "AutoSet-CS",
    10: "AutoSet for Her",
}


def _decode_mode(value: int) -> str:
    return _MODE_MAP.get(value, f"Mode({value})")
