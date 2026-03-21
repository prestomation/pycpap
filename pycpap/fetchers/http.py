"""HttpFetcher — fetches CPAP data files from an HTTP endpoint (e.g. EZ Share WiFi SD card)."""

import asyncio
import re
from datetime import date
from pathlib import Path

import aiofiles
import aiohttp

from .base import CPAPFetcher, FetchScope

# Files to always download from the SD card root
_SUMMARY_FILES = ["STR.EDF", "IDENTIFICATION.TXT"]

# EZ Share-style directory listing endpoint
_DIR_ENDPOINT = "/dir?dir=A:"
_DOWNLOAD_ENDPOINT = "/download"

# Maximum bytes allowed per downloaded file (50 MB)
MAX_FILE_BYTES = 50 * 1024 * 1024


def _safe_dest(dest_dir: Path, name: str) -> Path:
    """Return dest_dir/name, raising ValueError on path traversal attempt.

    Uses Path.relative_to() to validate containment without relying on
    filesystem state (avoids TOCTOU with resolve()).  The dest_dir itself
    is resolved once up-front; the constructed child path only uses the
    sanitised basename and therefore can never escape dest_dir regardless
    of symlinks in ``name``.
    """
    safe_name = Path(name).name  # takes only the final component, strips any ../
    if not safe_name or safe_name in (".", ".."):
        raise ValueError(f"Unsafe filename from EZ Share: {name!r}")
    dest_dir_resolved = dest_dir.resolve()
    candidate = dest_dir_resolved / safe_name
    try:
        candidate.relative_to(dest_dir_resolved)
    except ValueError:
        raise ValueError(f"Path traversal attempt blocked: {name!r}")
    return candidate


class HttpFetcher(CPAPFetcher):
    """Fetches CPAP data from an HTTP endpoint (EZ Share or compatible).

    The EZ Share WiFi SD card adapter exposes an HTTP server that serves
    files from the SD card. This fetcher uses aiohttp to download summary
    files (STR.EDF, IDENTIFICATION.TXT) and optionally DATALOG files.

    Args:
        base_url: Base URL of the HTTP server, e.g. ``http://192.168.4.1``.
            Trailing slashes are stripped.
        timeout_per_file: Per-file download timeout in seconds (default 30).
        total_timeout: Total session timeout in seconds (default 120).
    """

    def __init__(
        self,
        base_url: str,
        timeout_per_file: float = 30.0,
        total_timeout: float = 120.0,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout_per_file = timeout_per_file
        self.total_timeout = total_timeout

    async def _list_files(self, session: aiohttp.ClientSession) -> list[str]:
        """Fetch the directory listing from the SD card and return file names."""
        url = f"{self.base_url}{_DIR_ENDPOINT}"
        async with session.get(url) as resp:
            resp.raise_for_status()
            html = await resp.text()
        # Parse <a href="..."> links — EZ Share returns plain HTML with links
        return re.findall(r'href="[^"]*fname=([^"&]+)', html, re.IGNORECASE)

    async def _download_file(
        self,
        session: aiohttp.ClientSession,
        fname: str,
        fdir: str,
        dest_path: Path,
    ) -> None:
        """Download a single file from the SD card to dest_path.

        If an error occurs (including exceeding MAX_FILE_BYTES), the partially
        written destination file is removed to avoid orphaned partial files.
        """
        url = f"{self.base_url}{_DOWNLOAD_ENDPOINT}"
        params = {"fname": fname.upper(), "fdir": fdir}
        timeout = aiohttp.ClientTimeout(total=self.timeout_per_file)
        try:
            async with session.get(url, params=params, timeout=timeout) as resp:
                resp.raise_for_status()
                received = 0
                async with aiofiles.open(dest_path, "wb") as f:
                    async for chunk in resp.content.iter_chunked(65536):
                        # Check limit before writing so we never write a byte
                        # beyond MAX_FILE_BYTES, even within a single chunk.
                        if received + len(chunk) > MAX_FILE_BYTES:
                            raise RuntimeError(
                                f"Response exceeded {MAX_FILE_BYTES} bytes for {fname}"
                            )
                        received += len(chunk)
                        await f.write(chunk)
        except Exception:
            # Clean up the partial file before propagating the error
            try:
                dest_path.unlink(missing_ok=True)
            except OSError:
                pass
            raise

    async def fetch(
        self,
        dest_dir: Path,
        since: date | None = None,
        scope: FetchScope = FetchScope.SUMMARY_ONLY,
    ) -> None:
        """Fetch CPAP files from the HTTP endpoint to dest_dir."""
        dest_dir.mkdir(parents=True, exist_ok=True)
        total_timeout = aiohttp.ClientTimeout(total=self.total_timeout)

        async with aiohttp.ClientSession(timeout=total_timeout) as session:
            # Always download the summary files
            for fname in _SUMMARY_FILES:
                dest_path = _safe_dest(dest_dir, fname.upper())
                try:
                    await self._download_file(session, fname, "A:", dest_path)
                except aiohttp.ClientError as exc:
                    raise RuntimeError(
                        f"Failed to download {fname} from {self.base_url}: {exc}"
                    ) from exc

            if scope in (FetchScope.LAST_7_DAYS, FetchScope.ALL_AVAILABLE):
                # List the DATALOG directory and download subdirs
                try:
                    datalog_dir_url = f"{self.base_url}/dir?dir=A:/DATALOG"
                    async with session.get(datalog_dir_url) as resp:
                        if resp.status == 200:
                            html = await resp.text()
                            subdirs = re.findall(
                                r'href="[^"]*dir=A:/DATALOG/([^"&]+)"', html, re.IGNORECASE
                            )
                            datalog_dest = dest_dir / "DATALOG"
                            datalog_dest.mkdir(exist_ok=True)
                            for subdir in subdirs:
                                # Validate subdir name before using as path component
                                try:
                                    safe_subdir_path = _safe_dest(datalog_dest, subdir)
                                except ValueError:
                                    continue

                                if since is not None:
                                    # Subdir names are typically YYYYMMDD
                                    try:
                                        subdir_date = date(
                                            int(subdir[:4]),
                                            int(subdir[4:6]),
                                            int(subdir[6:8]),
                                        )
                                        if subdir_date < since:
                                            continue
                                    except (ValueError, IndexError):
                                        pass  # Not a date subdir; include it
                                # List and download files in the subdir
                                sub_url = f"{self.base_url}/dir?dir=A:/DATALOG/{subdir}"
                                async with session.get(sub_url) as sub_resp:
                                    if sub_resp.status != 200:
                                        continue
                                    sub_html = await sub_resp.text()
                                    files = re.findall(
                                        r'href="[^"]*fname=([^"&]+)', sub_html, re.IGNORECASE
                                    )
                                    sub_dest = safe_subdir_path
                                    sub_dest.mkdir(exist_ok=True)
                                    for file in files:
                                        # Validate filename before use as path component
                                        try:
                                            file_dest = _safe_dest(sub_dest, file.upper())
                                        except ValueError:
                                            continue
                                        await self._download_file(
                                            session, file, f"A:/DATALOG/{subdir}", file_dest
                                        )
                except aiohttp.ClientError:
                    # DATALOG is optional; don't fail if unavailable
                    pass
