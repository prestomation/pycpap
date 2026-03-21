from abc import ABC, abstractmethod
from datetime import date

from ..models import DeviceInfo, SleepSession


class CPAPReader(ABC):
    @abstractmethod
    async def get_sessions(self, since: date | None = None) -> list[SleepSession]:
        """Return a list of sleep sessions, optionally filtered by date.

        Args:
            since: Only return sessions on or after this date.

        Returns:
            List of SleepSession objects sorted by date ascending.
        """
        ...

    @abstractmethod
    async def get_device_info(self) -> DeviceInfo:
        """Return device metadata (model, serial, firmware).

        Returns:
            DeviceInfo populated from the SD card's identification file.
        """
        ...
