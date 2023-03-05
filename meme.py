"""Program to generate a meme given an image and a quote."""

import argparse
import os
import random

from meme_engine.meme_engine import MemeEngine
from quote_engine import Ingestor, QuoteModel
from quote_engine.utils import check_and_create_dirs


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    # Check to see whether the directories exist, if not, create them
    check_and_create_dirs()

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv",
        ]
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine("./_data/tmp")
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, nargs=1,
                        help="Path to an image file")
    parser.add_argument("--body", type=str, nargs=1,
                        help="Body to add to the image")
    parser.add_argument(
        "--author", type=str, nargs=1, help="Author to add to the image"
    )
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
