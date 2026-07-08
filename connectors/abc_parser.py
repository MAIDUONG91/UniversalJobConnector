from bs4 import BeautifulSoup

from models.job import Job


class ABCParser:

    def parse(self, html):

        soup = BeautifulSoup(html, "html.parser")

        jobs = []

        for item in soup.select(".job-item"):

            jobs.append(
                Job(
                    title=item.select_one(".title").text.strip(),
                    company=item.select_one(".company").text.strip(),
                    location=item.select_one(".location").text.strip(),
                    salary=item.select_one(".salary").text.strip(),
                    job_url=item.select_one("a")["href"],
                    source="ABC",
                    posted_date="",
                    crawled_at=datetime.now(),
                )
            )

        return jobs