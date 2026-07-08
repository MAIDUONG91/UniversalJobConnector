from datetime import datetime

from models.job import Job
from services.excel_reader import ExcelReader
from services.filter_service import FilterService
from services.report_service import ReportService


def main():

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

    print("Excel:", excel_file)

    print("HTML :", html_file)


if __name__ == "__main__":

    main()