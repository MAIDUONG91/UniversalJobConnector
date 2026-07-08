from abc import ABC, abstractmethod


class BaseConnector(ABC):
    """
    Base class của tất cả Connector.
    """

    @abstractmethod
    def connect(self):
        """Kết nối Website"""
        pass

    @abstractmethod
    def crawl(self):
        """Lấy dữ liệu"""
        pass

    @abstractmethod
    def parse(self):
        """Parse dữ liệu"""
        pass