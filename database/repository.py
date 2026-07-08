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
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
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

    def exists(self, job_url: str) -> bool:

        cursor = self.db.connection.cursor()

        cursor.execute(
            """
            SELECT 1
            FROM jobs
            WHERE job_url = ?
            LIMIT 1
            """,
            (job_url,),
        )

        return cursor.fetchone() is not None

    def count(self) -> int:

        cursor = self.db.connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM jobs
            """
        )

        return cursor.fetchone()[0]

    def get_all(self):

        cursor = self.db.connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM jobs
            ORDER BY id
            """
        )

        return cursor.fetchall()

    def delete_all(self):

        cursor = self.db.connection.cursor()

        cursor.execute(
            """
            DELETE FROM jobs
            """
        )

        self.db.connection.commit()

    def close(self):
        self.db.close()