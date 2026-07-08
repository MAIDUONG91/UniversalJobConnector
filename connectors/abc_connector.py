import requests

from connectors.base_connector import BaseConnector
from connectors.abc_parser import ABCParser
from utils.http_client import HttpClient


class ABCConnector(BaseConnector):

    def __init__(self):

        self.url = "https://www.vietnamworks.com/viec-lam?q=hr&l=29&sorting=lasted"
        self.parser = ABCParser()
        self.client = HttpClient()

    def connect(self):

        print(f"Connecting {self.url}")

        return self.client.get(self.url)

    def crawl(self):
        response = self.connect()
        html = response.text
        jobs = self.parser.parse(html)
        return jobs

    def parse(self):

        raise NotImplementedError