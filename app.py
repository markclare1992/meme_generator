import os
import random

import requests
from flask import Flask, abort, render_template, request

from meme_engine.meme_engine import MemeEngine
from quote_engine import Ingestor

app = Flask(__name__)

meme = MemeEngine("./static")
ingestor = Ingestor()


def setup():
    """Load all resources"""

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


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""
    img = imgs[random.randint(0, len(imgs) - 1)]
    quote = quotes[random.randint(0, len(quotes) - 1)]
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme"""
    image_url = request.form.get("image_url")
    if image_url is None:
        abort(400)

    response = requests.get(image_url, stream=True)
    if response.status_code != 200:
        abort(400)

    temp_file = os.path.join("_data/tmp", os.path.basename(image_url))
    with open(temp_file, "wb") as out_file:
        out_file.write(response.content)

    body = request.form.get("body")
    author = request.form.get("author")
    path = meme.make_meme(temp_file, body, author)

    os.remove(temp_file)

    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
