from abc import ABC, abstractmethod
from typing import Any, List


class IngestorInterface(ABC):
    """
    Abstract class for ingestors.
    """

    allowed_extensions: List[str] = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the file can be ingested by this ingestor.

        :param path: Path to the file.
        :return: True if the file can be ingested, False otherwise.
        """
        ext = path.split(".")[-1]

        try:
            if ext in cls.allowed_extensions:
                return True
            else:
                return False
        except Exception as e:
            print(f"Exception: {e}")
            return False

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Any]:
        """
        Parse the file and return a list of QuoteModel objects.

        :param path: Path to the file.
        :return: List of QuoteModel objects.
        """
        raise NotImplementedError("Subclass must implement abstract method")
