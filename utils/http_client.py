from __future__ import annotations

import requests


class HttpClient:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update(
            {
                "User-Agent":
                "UniversalJobConnector/1.0"
            }
        )

    def get(self, url: str) -> requests.Response:

        response = self.session.get(
            url,
            timeout=20,
        )

        response.raise_for_status()

        return response