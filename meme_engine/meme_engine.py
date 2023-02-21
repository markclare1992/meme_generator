import os
import random
from typing import Optional

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Meme Engine for creating memes"""

    def __init__(self, output_dir: str):
        """
        Constructor for the MemeEngine class
        :param output_dir: The directory to store output memes.
        """
        self.output_dir = output_dir

    def make_meme(
        self, img_path: str, text: str, author: str, width: int = 500
    ) -> Optional[str]:
        """Creates a meme given an image path and a quote body and author"""
        try:
            img = Image.open(img_path)
            new_width = width
            new_height = int(width * img.height / img.width)
            img = img.resize((new_width, new_height))
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("Chalkduster.ttf", size=15)
            text = f"{text} - {author}"
            text_width, text_height = font.getsize(text)

            # select random location for text to go
            text_location_x = random.randint(0, new_width)
            text_location_y = random.randint(0, new_height)

            if text_location_x + text_width > new_width:
                text_location_x = new_width - text_width
            if text_location_y + text_height > new_height:
                text_location_y = new_height - text_height

            draw.text((text_location_x, text_location_y), text, fill="white", font=font)
            output_path = os.path.join(
                self.output_dir, f"meme_{random.randint(0, 1000000)}.jpg"
            )
            img.save(output_path)
            return output_path
        except Exception as e:
            print(e)
            return None
