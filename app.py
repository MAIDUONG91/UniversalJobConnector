from datetime import datetime

from models.job import Job
from services.excel_reader import ExcelReader
from services.filter_service import FilterService
from services.report_service import ReportService
from services.email_service import EmailService
from utils.logger import get_logger


def main():
    logger = get_logger("UniversalJobConnector")

    logger.info("Application started")

    try:

        # Toàn bộ code hiện tại

        logger.info("Application finished successfully")

    except Exception:

        logger.exception("Application crashed")

        raise
    config = ExcelReader().load()

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

    filtered_jobs = FilterService().filter_jobs(
        jobs,
        config,
    )

    report = ReportService()

    excel_file = report.export_excel(filtered_jobs)

    html_file = report.export_html(filtered_jobs)
    EmailService().send(
        smtp_server="smtp.gmail.com",
        smtp_port=465,
        sender_email="EMAIL_GUI@gmail.com",
        sender_password="APP_PASSWORD",
        receiver_email="EMAIL_NHAN@gmail.com",
        subject="Universal Job Connector Report",
        html_file=html_file,
        excel_file=excel_file,
    )

    print("Đã gửi email thành công.")

    print("Excel:", excel_file)

    print("HTML :", html_file)


if __name__ == "__main__":

    main()