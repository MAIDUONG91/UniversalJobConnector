from __future__ import annotations

import sqlite3
from pathlib import Path


class Database:

    def __init__(self):

        Path("data").mkdir(exist_ok=True)

        self.connection = sqlite3.connect(
            "data/jobs.db"
        )

        self.connection.row_factory = sqlite3.Row

    def create_tables(self):

        cursor = self.connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT,

            company TEXT,

            location TEXT,

            salary TEXT,

            job_url TEXT,

            source TEXT,

            posted_date TEXT,

            crawled_at TEXT
        )
        """)

        self.connection.commit()

    def close(self):

        self.connection.close()