from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Đọc cấu hình từ file .env."""

    SMTP_SERVER: str = os.getenv(
        "SMTP_SERVER",
        "smtp.gmail.com",
    )

    SMTP_PORT: int = int(
        os.getenv(
            "SMTP_PORT",
            "465",
        )
    )

    EMAIL_ADDRESS: str = os.getenv(
        "EMAIL_ADDRESS",
        "",
    )

    EMAIL_APP_PASSWORD: str = os.getenv(
        "EMAIL_APP_PASSWORD",
        "",
    )

    REPORT_EMAIL: str = os.getenv(
        "REPORT_EMAIL",
        "",
    )

    SCHEDULE_TIME: str = os.getenv(
        "SCHEDULE_TIME",
        "09:00",
    )


settings = Settings()