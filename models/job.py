from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Job:
    title: str
    company: str
    location: str
    salary: str
    job_url: str
    source: str
    posted_date: str | None = None
    crawled_at: datetime | None = None