"""Ingestor class to parse the file and return a list of QuoteModel objects."""
from typing import Any, List

from .csv_ingestor import CSVIngestor
from .docx_ingestor import DocxIngestor
from .ingestor_interface import IngestorInterface
from .pdf_ingestor import PDFIngestor
from .text_ingestor import TextIngestor


class Ingestor(IngestorInterface):
    """
    Ingestor class to parse the file and return a list of QuoteModel objects.

    This class will use the appropriate ingestor to parse the file.
    """

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[Any]:
        """
        Parse the file and return a list of QuoteModel objects.

        :param path: Path to the file.

        :return: List of QuoteModel objects.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise Exception("Ingestion failed.")
