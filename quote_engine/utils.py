import os
from typing import Any, List

from .quote_model import QuoteModel


def get_quote_list_from_text_file(path: str, delete_file: bool = False) -> List[Any]:
    """
    Parse the text file and return a list of QuoteModel objects.
    If delete_file is True, the file will be deleted after parsing.

    :param path: Path to the file.
    :param delete_file: If True, the file will be deleted after parsing.

    :return: List of QuoteModel objects.
    """
    quotes = []
    try:
        with open(path, "r", encoding="utf-8-sig") as f:
            for line in f:
                line = line.strip("\n\r").strip()
                if len(line) > 0:
                    parse = line.split("-")
                    body = parse[0].strip().strip('"')
                    author = parse[1].strip().strip('"')

                    new_quote = QuoteModel(body, author)
                    quotes.append(new_quote)
    except FileNotFoundError as e:
        print(f"Exception: {e}. File not found: {path}")
        return quotes
    except Exception as e:
        print(f"Exception: {e}. Failed to parse file: {path}")
        return quotes

    if delete_file:
        try:
            os.remove(path)
        except Exception as e:
            print(f"Exception: {e}. Failed to delete file: {path}")

    return quotes
