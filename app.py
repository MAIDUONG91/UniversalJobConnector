from datetime import datetime

from database.repository import JobRepository
from models.job import Job


def main():

    repository = JobRepository()

    job = Job(
        title="HR Executive",
        company="ABC Company",
        location="Ho Chi Minh",
        salary="20,000,000",
        job_url="https://ABCweb.com/job/1",
        source="ABC",
        posted_date="2026-07-08",
        crawled_at=datetime.now(),
    )

    repository.save(job)

    repository.close()

    print("Save Success")


if __name__ == "__main__":
    main()