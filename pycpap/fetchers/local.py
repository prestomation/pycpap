"""LocalFetcher — copies CPAP data from a locally mounted SD card path."""

import shutil
from datetime import date
from pathlib import Path

import aiofiles
import aiofiles.os

from .base import CPAPFetcher, FetchScope

_SUMMARY_FILES = ["STR.EDF", "IDENTIFICATION.TXT"]


class LocalFetcher(CPAPFetcher):
    """Fetches CPAP data by copying files from a locally mounted path.

    Useful when the SD card is mounted directly (e.g. via a card reader)
    or when a network share is already mounted at a local path.

    Args:
        path: Path to the root of the CPAP SD card (the directory that
            contains STR.EDF, IDENTIFICATION.TXT, DATALOG/, etc.).
    """

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    async def fetch(
        self,
        dest_dir: Path,
        since: date | None = None,
        scope: FetchScope = FetchScope.SUMMARY_ONLY,
    ) -> None:
        """Copy CPAP files from the mounted path to dest_dir."""
        dest_dir.mkdir(parents=True, exist_ok=True)

        # Copy summary files (case-insensitive search for portability)
        for fname in _SUMMARY_FILES:
            src = self._find_file(self.path, fname)
            if src is None:
                raise FileNotFoundError(
                    f"{fname} not found in {self.path}. "
                    "Ensure the SD card is mounted and the path is correct."
                )
            dest = dest_dir / fname.upper()
            await self._copy_file(src, dest)

        if scope in (FetchScope.LAST_7_DAYS, FetchScope.ALL_AVAILABLE):
            datalog_src = self.path / "DATALOG"
            if datalog_src.exists():
                datalog_dest = dest_dir / "DATALOG"
                datalog_dest.mkdir(exist_ok=True)
                for subdir in datalog_src.iterdir():
                    if not subdir.is_dir():
                        continue
                    if since is not None:
                        try:
                            subdir_date = date(
                                int(subdir.name[:4]),
                                int(subdir.name[4:6]),
                                int(subdir.name[6:8]),
                            )
                            if subdir_date < since:
                                continue
                        except (ValueError, IndexError):
                            pass  # Not a date subdir; include it
                    sub_dest = datalog_dest / subdir.name
                    sub_dest.mkdir(exist_ok=True)
                    for file in subdir.iterdir():
                        if file.is_file():
                            await self._copy_file(file, sub_dest / file.name.upper())

    @staticmethod
    def _find_file(directory: Path, name: str) -> Path | None:
        """Find a file case-insensitively in directory."""
        name_upper = name.upper()
        for candidate in directory.iterdir():
            if candidate.name.upper() == name_upper and candidate.is_file():
                return candidate
        return None

    @staticmethod
    async def _copy_file(src: Path, dest: Path) -> None:
        """Async file copy using aiofiles."""
        async with aiofiles.open(src, "rb") as fsrc:
            async with aiofiles.open(dest, "wb") as fdest:
                while True:
                    chunk = await fsrc.read(65536)
                    if not chunk:
                        break
                    await fdest.write(chunk)
