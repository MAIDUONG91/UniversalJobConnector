from __future__ import annotations

import mimetypes
import smtplib
from email.message import EmailMessage
from pathlib import Path


class EmailService:

    def send(
        self,
        smtp_server: str,
        smtp_port: int,
        sender_email: str,
        sender_password: str,
        receiver_email: str,
        subject: str,
        html_file: Path,
        excel_file: Path,
    ) -> None:

        message = EmailMessage()

        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        html_content = html_file.read_text(
            encoding="utf-8"
        )

        message.set_content(
            "Vui lòng xem báo cáo việc làm trong tệp đính kèm."
        )

        message.add_alternative(
            html_content,
            subtype="html",
        )

        for file_path in (html_file, excel_file):

            mime_type, _ = mimetypes.guess_type(file_path)

            if mime_type is None:
                maintype = "application"
                subtype = "octet-stream"
            else:
                maintype, subtype = mime_type.split("/")

            with open(file_path, "rb") as file:

                message.add_attachment(
                    file.read(),
                    maintype=maintype,
                    subtype=subtype,
                    filename=file_path.name,
                )

        with smtplib.SMTP_SSL(
            smtp_server,
            smtp_port,
        ) as smtp:

            smtp.login(
                sender_email,
                sender_password,
            )

            smtp.send_message(message)