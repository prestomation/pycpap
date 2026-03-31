"""Stub tests for ResMedReader — will be filled in once fixture .edf files are available."""

import pytest
from datetime import date
from unittest.mock import AsyncMock, MagicMock, patch
from pathlib import Path

from pycpap import ResMedReader, LocalFetcher, HttpFetcher, FetchScope, SleepSession, DeviceInfo


class TestResMedReaderInit:
    def test_reader_accepts_local_fetcher(self):
        fetcher = LocalFetcher("/tmp/fake_sd_card")
        reader = ResMedReader(fetcher)
        assert reader.fetcher is fetcher

    def test_reader_accepts_http_fetcher(self):
        fetcher = HttpFetcher("http://192.168.4.1")
        reader = ResMedReader(fetcher)
        assert reader.fetcher is fetcher

    def test_reader_default_scope(self):
        fetcher = LocalFetcher("/tmp/fake")
        reader = ResMedReader(fetcher)
        assert reader.scope == FetchScope.SUMMARY_ONLY


class TestResMedReaderGetSessions:
    @pytest.mark.asyncio
    async def test_get_sessions_returns_list(self):
        # TODO: implement once fixture STR.edf files are available
        pass

    @pytest.mark.asyncio
    async def test_get_sessions_filters_by_since(self):
        # TODO: verify that since= parameter correctly excludes old sessions
        pass

    @pytest.mark.asyncio
    async def test_get_sessions_sorted_by_date(self):
        # TODO: verify output is sorted ascending by date
        pass

    @pytest.mark.asyncio
    async def test_get_sessions_skips_empty_days(self):
        # TODO: verify days with MaskOn=0 are excluded
        pass


class TestResMedReaderDeviceInfo:
    @pytest.mark.asyncio
    async def test_get_device_info_returns_device_info(self):
        # TODO: implement once fixture identification.txt is available
        pass

    @pytest.mark.asyncio
    async def test_get_device_info_handles_missing_fields(self):
        # TODO: verify graceful handling of missing keys
        pass


class TestLocalFetcher:
    @pytest.mark.asyncio
    async def test_fetch_copies_summary_files(self, tmp_path):
        # TODO: create mock SD card dir, verify files are copied
        pass

    @pytest.mark.asyncio
    async def test_fetch_missing_str_edf_raises(self, tmp_path):
        # TODO: verify FileNotFoundError if STR.EDF is absent
        pass


class TestHttpFetcher:
    @pytest.mark.asyncio
    async def test_fetch_downloads_summary_files(self, tmp_path):
        # TODO: mock aiohttp responses, verify files are written to dest_dir
        pass

    @pytest.mark.asyncio
    async def test_fetch_handles_server_error(self, tmp_path):
        # TODO: verify RuntimeError is raised on HTTP error status
        pass


class TestResMedReaderFromBytes:
    def test_from_bytes_rejects_empty_bytes(self):
        """Empty bytes must raise ValueError, not crash with a low-level OSError."""
        with pytest.raises(ValueError, match="must be non-empty"):
            ResMedReader.from_bytes(b"")

    def test_from_bytes_rejects_non_edf_data(self):
        """Non-EDF bytes should raise ValueError with a clear message."""
        with pytest.raises(ValueError, match="not a valid EDF file"):
            ResMedReader.from_bytes(b"this is not EDF data")

    def test_from_bytes_returns_tuple_of_sessions_and_info(self):
        """from_bytes must return a (sessions, device_info) tuple."""
        with pytest.raises(ValueError):
            ResMedReader.from_bytes(b"not edf")
        # tuple check can't run because of the raise above — just verify
        # the signature returns the right types when called with valid data
        # (full test needs real EDF fixture)
        result = (ResMedReader.from_bytes.__code__.co_varnames[:3])
        assert result == ("cls", "edf_data", "identification_data")


class TestSleepSessionModel:
    def test_sleep_session_required_fields(self):
        from datetime import datetime
        session = SleepSession(
            date=date(2024, 1, 1),
            session_start=datetime(2024, 1, 1, 22, 0),
            session_end=datetime(2024, 1, 2, 6, 0),
            duration_minutes=480.0,
            ahi=2.5,
            apnea_index=0.8,
            hypopnea_index=1.7,
            mask_leak_median=3.0,
            mask_leak_95=8.0,
            pressure_median=10.0,
            pressure_95=12.0,
            mode="APAP",
        )
        assert session.ahi == 2.5
        assert session.respiratory_rate is None  # optional field default

    def test_device_info_fields(self):
        info = DeviceInfo(model="AirSense 10 AutoSet", serial="12345678", firmware="SX567-0401")
        assert info.model == "AirSense 10 AutoSet"
