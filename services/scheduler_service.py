from __future__ import annotations

import time

import schedule

from utils.logger import get_logger

logger = get_logger(__name__)


class SchedulerService:
    """Service quản lý lịch chạy công việc."""

    def __init__(self) -> None:
        logger.info("SchedulerService initialized.")

    def add_daily_job(
        self,
        run_time: str,
        callback,
    ) -> None:
        """
        Đăng ký một công việc chạy hằng ngày.

        Ví dụ:
            add_daily_job("09:00", run_job)
        """
        schedule.every().day.at(run_time).do(callback)

        logger.info(
            "Scheduled daily job at %s",
            run_time,
        )

    def start(self) -> None:
        """Bắt đầu vòng lặp Scheduler."""

        logger.info("Scheduler started.")

        while True:
            schedule.run_pending()
            time.sleep(1)