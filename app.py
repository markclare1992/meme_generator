"""This module is the main entry point of the application."""
import os
import random

import requests
from flask import Flask, render_template, request

from meme_engine.meme_engine import MemeEngine
from quote_engine import Ingestor
from quote_engine.utils import check_and_create_dirs

app = Flask(__name__)

meme = MemeEngine("./static")
ingestor = Ingestor()


def setup():
    """Load all resources."""
    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]
    quotes = []
    for f in quote_files:
        quotes.extend(ingestor.parse(f))
    images_path = "_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


check_and_create_dirs()
quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme."""
    img = imgs[random.randint(0, len(imgs) - 1)]
    quote = quotes[random.randint(0, len(quotes) - 1)]
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information."""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme."""
    try:
        image_url = request.form.get("image_url")
        response = requests.get(image_url, stream=True)
        temp_file = os.path.join("_data/tmp", os.path.basename(image_url))
        with open(temp_file, "wb") as out_file:
            out_file.write(response.content)

        body = request.form.get("body")
        author = request.form.get("author")
        path = meme.make_meme(temp_file, body, author)

        os.remove(temp_file)

    except requests.exceptions.ConnectionError:
        print("<Enter user friendly error message>")
        return render_template("meme_error.html")
    except Exception as e:
        print(f"Exception: {e}")
        return render_template("meme_error.html")

    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
