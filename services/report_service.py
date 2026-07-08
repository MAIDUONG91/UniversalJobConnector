from __future__ import annotations

from pathlib import Path

from openpyxl import Workbook

from models.job import Job


class ReportService:

    def __init__(self):

        self.output_dir = Path("output")

        self.output_dir.mkdir(exist_ok=True)

    def export_excel(
        self,
        jobs: list[Job],
    ) -> Path:

        workbook = Workbook()

        sheet = workbook.active

        sheet.title = "Jobs"

        sheet.append([
            "Title",
            "Company",
            "Location",
            "Salary",
            "Job URL",
            "Source",
            "Posted Date",
        ])

        for job in jobs:

            sheet.append([
                job.title,
                job.company,
                job.location,
                job.salary,
                job.job_url,
                job.source,
                job.posted_date,
            ])

        file_path = self.output_dir / "report.xlsx"

        workbook.save(file_path)

        workbook.close()

        return file_path

    def export_html(
        self,
        jobs: list[Job],
    ) -> Path:

        rows = ""

        for job in jobs:

            rows += f"""
<tr>
<td>{job.title}</td>
<td>{job.company}</td>
<td>{job.location}</td>
<td>{job.salary}</td>
<td><a href="{job.job_url}">Open</a></td>
</tr>
"""

        html = f"""
<!DOCTYPE html>
<html lang="vi">

<head>
<meta charset="utf-8">

<title>Job Report</title>

<style>

body{{font-family:Arial;}}

table{{border-collapse:collapse;width:100%;}}

th,td{{border:1px solid #ddd;padding:8px;}}

th{{background:#4CAF50;color:white;}}

</style>

</head>

<body>

<h2>Universal Job Connector Report</h2>

<table>

<tr>

<th>Title</th>

<th>Company</th>

<th>Location</th>

<th>Salary</th>

<th>Link</th>

</tr>

{rows}

</table>

</body>

</html>
"""

        file_path = self.output_dir / "report.html"

        file_path.write_text(
            html,
            encoding="utf-8",
        )

        return file_path