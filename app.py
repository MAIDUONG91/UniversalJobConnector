from __future__ import annotations

from datetime import datetime

from models.job import Job
from services.email_service import EmailService
from services.excel_reader import ExcelReader
from services.filter_service import FilterService
from services.report_service import ReportService
from services.scheduler_service import SchedulerService
from utils.logger import get_logger
from config.settings import settings


logger = get_logger("UniversalJobConnector")


def run_job() -> None:
    """Thực hiện toàn bộ quy trình của Universal Job Connector Framework."""

    logger.info("========== Job Started ==========")

    try:
        # Đọc cấu hình bộ lọc từ Excel
        config = ExcelReader().load()

        # ------------------------------------------------------------------
        # Tạm thời dùng dữ liệu mẫu.
        # Sau này sẽ thay bằng:
        # jobs = ABCConnector().crawl()
        # ------------------------------------------------------------------
        jobs = [
            Job(
                title="HR Executive",
                company="ABC Company",
                location="Hồ Chí Minh",
                salary="20000000",
                job_url="https://ABCweb.com/job/1",
                source="ABC",
                posted_date="2026-07-08",
                crawled_at=datetime.now(),
            ),
            Job(
                title="Python Developer",
                company="XYZ Company",
                location="Đà Nẵng",
                salary="35000000",
                job_url="https://ABCweb.com/job/2",
                source="ABC",
                posted_date="2026-07-08",
                crawled_at=datetime.now(),
            ),
        ]

        logger.info("Loaded %s jobs.", len(jobs))

        # Lọc dữ liệu
        filtered_jobs = FilterService().filter_jobs(
            jobs,
            config,
        )

        logger.info(
            "Filtered jobs: %s",
            len(filtered_jobs),
        )

        # Sinh báo cáo
        report = ReportService()

        excel_file = report.export_excel(filtered_jobs)
        html_file = report.export_html(filtered_jobs)

        logger.info("Report generated.")

        # Gửi email
        EmailService().send(
            smtp_server=settings.SMTP_SERVER,
            smtp_port=settings.SMTP_PORT,
            sender_email=settings.EMAIL_ADDRESS,
            sender_password=settings.EMAIL_APP_PASSWORD,
            receiver_email=settings.REPORT_EMAIL,
            subject="Universal Job Connector Report",
            html_file=html_file,
            excel_file=excel_file,
    )

        logger.info("Email sent successfully.")

        print(f"Excel : {excel_file}")
        print(f"HTML  : {html_file}")

    except Exception:
        logger.exception("Job failed.")
        raise

    logger.info("========== Job Finished ==========")


def main() -> None:
    """Khởi động Scheduler."""

    logger.info("Application started.")

    scheduler = SchedulerService()

    scheduler.add_daily_job(
        settings.SCHEDULE_TIME,
        run_job,
    )

    logger.info("Scheduler is waiting for scheduled jobs...")

    scheduler.start()


if __name__ == "__main__":
    main()