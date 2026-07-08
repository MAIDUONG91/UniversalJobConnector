from __future__ import annotations

from abc import ABC, abstractmethod

from models.job import Job


class BaseParser(ABC):

    @abstractmethod
    def parse(self, raw_data: str) -> list[Job]:
        """
        Chuyển dữ liệu thô thành danh sách Job.
        """
        raise NotImplementedError