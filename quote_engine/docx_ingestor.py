from typing import Any, List

from docx import Document

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class DocxIngestor(IngestorInterface):
    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path) -> List[Any]:
        # Should never reach below, as can_ingest should have been called first. But just in case.
        if not cls.can_ingest(path):
            raise Exception("Ingestion failed.")

        quotes = []
        try:
            doc = Document(path)
            for para in doc.paragraphs:
                if para.text != "":
                    parse = para.text.split(" - ")
                    # Check that parse has 2 elements, and that both elements are not empty.
                    if len(parse) == 2 and parse[0] != "" and parse[1] != "":
                        body = parse[0].strip().strip('"')
                        author = parse[1].strip().strip('"')
                        new_quote = QuoteModel(body, author)
                        quotes.append(new_quote)

        except FileNotFoundError as e:
            print(f"File at path {path} not found: {e}. File not parsed.")
            return quotes

        except Exception as e:
            print(f"Exception: {e}. File not parsed.")
            return quotes

        return quotes
