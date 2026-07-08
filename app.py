from datetime import datetime

from models.job import Job
from services.excel_reader import ExcelReader
from services.filter_service import FilterService


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

        Job(
            title="HR Assistant",
            company="DEF Company",
            location="Hồ Chí Minh",
            salary="12000000",
            job_url="https://ABCweb.com/job/3",
            source="ABC",
            posted_date="2026-07-08",
            crawled_at=datetime.now(),
        ),
    ]

    service = FilterService()

    result = service.filter_jobs(jobs, config)

    print(f"Tổng Job ban đầu: {len(jobs)}")

    print(f"Job sau khi lọc: {len(result)}")

    print()

    for job in result:

        print(job.title)

        print(job.company)

        print(job.location)

        print(job.salary)

        print("-" * 40)


if __name__ == "__main__":
    main()