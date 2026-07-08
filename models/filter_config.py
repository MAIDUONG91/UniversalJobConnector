from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class FilterConfig:
    keyword: str
    location: str
    min_salary: int
    max_salary: int