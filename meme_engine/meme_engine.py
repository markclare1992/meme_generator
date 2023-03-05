"""Meme Engine for creating memes."""
import os
import random
import textwrap
from typing import Optional

from PIL import Image, ImageDraw, ImageFont


def caption_image(author, draw, new_height, new_width, text):
    """Add text to the image."""
    body_font_size = 20
    author_font_size = 36
    body_font = ImageFont.truetype("Chalkduster.ttf", body_font_size)
    author_font = ImageFont.truetype("Chalkduster.ttf", author_font_size)

    # Get size of text with initial font sizes
    body_width, body_height = draw.multiline_textsize(text, font=body_font)
    author_width, author_height = draw.multiline_textsize(author,
                                                          font=author_font)

    # Determine font size that fits text within image bounds
    body_font_size = int(body_font_size * (new_width / body_width) * 0.9)
    author_font_size = int(author_font_size * (new_width / author_width) * 0.9)
    body_font = ImageFont.truetype("Chalkduster.ttf", body_font_size)
    author_font = ImageFont.truetype("Chalkduster.ttf", author_font_size)

    # Wrap text with new font sizes
    body_lines = textwrap.wrap(text, width=new_width//5)
    author_lines = textwrap.wrap(author, width=new_width//5)

    # Get size of text with new font sizes
    body_width, body_height = draw.multiline_textsize(text, font=body_font)
    author_width, author_height = draw.multiline_textsize(author,
                                                          font=author_font)

    # Randomize starting position for body text
    body_x = random.randint(0, new_width - body_width)
    body_y = random.randint(0, new_height - body_height)

    # Adjust starting position if body text is outside of image bounds
    if body_x + body_width > new_width:
        body_x = new_width - body_width
    if body_y + body_height > new_height:
        body_y = new_height - body_height

    # Set starting position for author text
    author_x = body_x
    author_y = body_y + body_height + 10

    # Adjust starting position if author text is outside of image bounds
    if author_y + author_height > new_height:
        author_y = body_y - author_height - 10

    # Draw body text
    for line in body_lines:
        draw.text((body_x, body_y), line, font=body_font,
                  fill=(255, 255, 255))
        body_y += body_font.getsize(line)[1]

    # Draw author text
    for line in author_lines:
        draw.text((author_x, author_y), line, font=author_font,
                  fill=(255, 255, 255))
        author_y += author_font.getsize(line)[1]


class MemeEngine:
    """Meme Engine for creating memes."""

    def __init__(self, output_dir: str):
        """
        Initialise the MemeEngine class.

        :param output_dir: The directory to store output memes.
        """
        self.output_dir = output_dir

    def make_meme(
        self, img_path: str, text: str, author: str, width: int = 500
    ) -> Optional[str]:
        """Create a meme given an image path and a quote body and author."""
        try:
            author = f"Author - {author}"
            img = Image.open(img_path)
            new_width = width
            new_height = int(width * img.height / img.width)
            img = img.resize((new_width, new_height))
            draw = ImageDraw.Draw(img)
            caption_image(author, draw, new_height, new_width, text)

            output_path = os.path.join(
                self.output_dir, f"meme_{random.randint(0, 1000000)}.jpg"
            )
            img.save(output_path)
            return output_path
        except Exception as e:
            print(e)
            return None
