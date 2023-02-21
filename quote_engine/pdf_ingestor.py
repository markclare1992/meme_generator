import random
import subprocess
from typing import Any, List

from .ingestor_interface import IngestorInterface
from .utils import get_quote_list_from_text_file


class PDFIngestor(IngestorInterface):
    """
    PDF ingestor class to parse the .pdf files using xpdf & subprocesses and return a list of QuoteModel objects.
    """

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[Any]:
        """
        Parse the pdf file and return a list of QuoteModel objects.

        :param path: Path to the file.

        :return: List of QuoteModel objects.
        """
        # Should never reach below, as can_ingest should have been called first. But just in case.
        if not cls.can_ingest(path):
            raise Exception("Ingestion failed.")

        tmp = f"./_data/tmp/{random.randint(0, 1000000)}.txt"
        call = subprocess.call(["pdftotext", "-layout", path, tmp])
        if call != 0:
            raise Exception("PDF to text conversion failed.")
        quotes = get_quote_list_from_text_file(tmp, True)
        return quotes
