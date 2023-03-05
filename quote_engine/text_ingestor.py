"""Text ingestor class to parse the .txt files."""
from typing import Any, List

from .ingestor_interface import IngestorInterface
from .utils import get_quote_list_from_text_file


class TextIngestor(IngestorInterface):
    """Text ingestor class to parse the .txt files."""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[Any]:
        """
        Parse the text file and return a list of QuoteModel objects.

        :param path: Path to the file.

        :return: List of QuoteModel objects.
        """
        # Should never reach below, as can_ingest should have been called
        # first. But just in case.
        if not cls.can_ingest(path):
            raise Exception("Ingestion failed.")
        # Text ingestor will not depend on subprocess to delete the file,
        # can reuse the same function in pdf ingestor.
        quotes = get_quote_list_from_text_file(path, False)
        return quotes
