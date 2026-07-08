from __future__ import annotations

from models.job import Job
from database.database import Database


class JobRepository:

    def __init__(self):

        self.db = Database()

        self.db.create_tables()

    def save(self, job: Job):

        cursor = self.db.connection.cursor()

        cursor.execute(
            """
            INSERT INTO jobs(
                title,
                company,
                location,
                salary,
                job_url,
                source,
                posted_date,
                crawled_at
            )

            VALUES(?,?,?,?,?,?,?,?)
            """,
            (
                job.title,
                job.company,
                job.location,
                job.salary,
                job.job_url,
                job.source,
                job.posted_date,
                str(job.crawled_at),
            ),
        )

        self.db.connection.commit()

    def close(self):

        self.db.close()