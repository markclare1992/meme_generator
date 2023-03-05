"""CSV ingestor class to parse the .csv files."""
from typing import Any, List

import pandas as pd

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    """CSV ingestor class to parse the .csv files."""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[Any]:
        """
        Parse the csv file and return a list of QuoteModel objects.

        :param path: Path to the file.

        :return: List of QuoteModel objects.
        """
        # Should never reach below, as can_ingest should have been called
        # first. But just in case.
        if not cls.can_ingest(path):
            raise Exception("Ingestion failed.")

        quotes = []
        try:
            df = pd.read_csv(path, header=0)
            for index, row in df.iterrows():
                body = row["body"].strip().strip('"')
                author = row["author"].strip().strip('"')
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)
        except FileNotFoundError as e:
            print(f"File at path {path} not found: {e}. File not parsed.")
            return quotes
        except Exception as e:
            print(f"Exception: {e}. File not parsed.")
            return quotes

        return quotes
