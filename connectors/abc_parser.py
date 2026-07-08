from __future__ import annotations

from utils.parser import BaseParser
from models.job import Job


class ABCParser(BaseParser):

    def parse(self, raw_data: str) -> list[Job]:

        print("Parser đang xử lý dữ liệu...")

        # Version 1.4:
        # Chưa parse HTML thật.
        # Chỉ trả về danh sách rỗng.

        return []