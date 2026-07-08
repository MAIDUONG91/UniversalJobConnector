from __future__ import annotations

from models.filter_config import FilterConfig
from models.job import Job


class FilterService:

    def filter_jobs(
        self,
        jobs: list[Job],
        config: FilterConfig,
    ) -> list[Job]:

        result: list[Job] = []

        for job in jobs:

            if not self._match_keyword(job, config):
                continue

            if not self._match_location(job, config):
                continue

            if not self._match_salary(job, config):
                continue

            result.append(job)

        return result

    def _match_keyword(
        self,
        job: Job,
        config: FilterConfig,
    ) -> bool:

        keyword = config.keyword.lower()

        return (
            keyword in job.title.lower()
            or keyword in job.company.lower()
        )

    def _match_location(
        self,
        job: Job,
        config: FilterConfig,
    ) -> bool:

        return config.location.lower() in job.location.lower()

    def _match_salary(
        self,
        job: Job,
        config: FilterConfig,
    ) -> bool:

        try:
            salary = int(
                str(job.salary).replace(",", "")
            )
        except ValueError:
            return False

        return (
            config.min_salary
            <= salary
            <= config.max_salary
        )