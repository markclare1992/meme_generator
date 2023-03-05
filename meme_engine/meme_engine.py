"""Meme Engine for creating memes."""
import os
import random
import textwrap
from typing import Optional

from PIL import Image, ImageDraw, ImageFont


def caption_image(author, draw, new_height, new_width, text):
    """Add text to the image."""
    try:
        font_body = ImageFont.truetype("Chalkduster.ttf", size=20)
        font_author = ImageFont.truetype("Chalkduster.ttf", size=30)
        text_lines = textwrap.wrap(text, width=20)
        text_width, text_height = font_body.getsize(text)
        # select random location for text to go
        text_location_x = random.randint(0, new_width)
        text_location_y = random.randint(0, new_height)
        if text_location_x + text_width > new_width:
            text_location_x = new_width - text_width
        if text_location_y + text_height > new_height:
            text_location_y = new_height - text_height
        for line in text_lines:
            draw.text(
                (text_location_x, text_location_y),
                line,
                fill="white",
                font=font_body,
                align="center",
            )
            text_location_y += text_height
        draw.text(
            (text_location_x, text_location_y),
            author,
            fill="white",
            font=font_author,
            align="center",
        )

    except Exception as e:
        print(e)
        return None


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
