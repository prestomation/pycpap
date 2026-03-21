from enum import Enum
from abc import ABC, abstractmethod
from pathlib import Path
from datetime import date


class FetchScope(Enum):
    SUMMARY_ONLY = "summary_only"
    LAST_7_DAYS = "last_7_days"
    ALL_AVAILABLE = "all_available"


class CPAPFetcher(ABC):
    @abstractmethod
    async def fetch(
        self,
        dest_dir: Path,
        since: date | None = None,
        scope: FetchScope = FetchScope.SUMMARY_ONLY,
    ) -> None:
        """Fetch CPAP data files to dest_dir.

        Args:
            dest_dir: Directory to write fetched files into.
            since: Only fetch data since this date (optional).
            scope: Controls which files to fetch.
        """
        ...
