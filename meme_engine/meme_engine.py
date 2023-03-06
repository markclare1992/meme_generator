"""Meme Engine for creating memes."""
import os
import random
import textwrap
from typing import Optional

from PIL import Image, ImageDraw, ImageFont


def _text_wrap(text, font, max_width):
    """
    Wrap text based on specified width.

    Args:
        text: Text to wrap.
        font: PIL ImageFont object.
        max_width: Maximum width of the text.

    Returns:
        A list of lines that contain the wrapped text.
    """
    lines = textwrap.wrap(text, width=max_width // font.getsize('x')[0])
    return lines


def add_image_caption(image, caption_text, caption_author):
    """
    Add a caption to an image.

    Args:
        image: PIL Image object.
        caption_text: Text to display as the caption.
        caption_author: Author of the caption.

    Returns:
        PIL Image object with the caption added.
    """
    draw = ImageDraw.Draw(image)

    if not caption_text or not caption_author:
        return image

    font_size = 20
    font = ImageFont.truetype("Chalkduster.ttf", font_size)

    try:
        # Calculate x axis to display text
        x_min = (image.size[0] * 8) // 100  # 8%
        x_max = (image.size[0] * 50) // 100  # 50%
        range_x = random.randint(x_min, x_max)

        # Split text based on font and random position x
        lines = _text_wrap(caption_text, font, image.size[0] - range_x)
        line_height = font.getsize('hg')[1]  # Get line spacing

        # Calculate y axis for text display
        y_min = (image.size[1] * 4) // 100  # 4%
        y_max = (image.size[1] * 90) // 100  # 90%
        y_max -= len(lines) * line_height  # adjust based on number of lines
        range_y = random.randint(y_min, y_max)

        # draw text
        for line in lines:
            draw.text((range_x, range_y), line, font=font, align="left")
            range_y += line_height

        # Calculate x and y axis to display author
        range_y += 5
        range_x += 20

        # draw author
        draw.text((range_x, range_y), f'- {caption_author}',
                  font=font, align='left')

        return image

    except Exception as e:
        print(e)
        return image


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
            resized_img = img.resize((new_width, new_height))
            captioned_img = add_image_caption(resized_img, text, author)
            output_path = os.path.join(
                self.output_dir, f"meme_{random.randint(0, 1000000)}.jpg"
            )
            captioned_img.save(output_path)
            return output_path
        except Exception as e:
            print(e)
            return None
