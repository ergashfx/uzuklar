import math

from PIL import Image, ImageDraw, ImageFont
import os


def add_text_to_image(image_path, text, font_path, font_size, font_color, position, angle, output_path):
    original_img = Image.open(image_path).convert("RGBA")
    text_layer = Image.new("RGBA", original_img.size, (255, 255, 255, 0))
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(text_layer)
    text_width, text_height = draw.textsize(text, font=font)
    text_position = (position[0] - text_width / 2, position[1] - text_height / 2)
    draw.text(text_position, text, font=font, fill=font_color, align="center", spacing=0, stroke_width=0)
    text_layer = text_layer.rotate(angle, expand=True)
    text_layer = text_layer.resize(original_img.size)
    result = Image.alpha_composite(original_img, text_layer)
    result.save(output_path)


def add_text_to_image_1(text):
    add_text_to_image(
        "images/image1.jpg",
        text,
        "images/myfont.ttf",
        200,
        (0, 0, 0),
        (1270, 1610),
        -20,  # Angle
        "images/saved/image1.png"
    )


def add_text_to_image_2(text):
    return add_text_to_image(
        "images/image2.jpg",
        text,
        "images/fontim.otf",
        90,
        (250, 244, 184),
        (520, 490),
        0,
        "images/saved/image2.png"

    )

def add_text_to_image_3(text):
    return add_text_to_image(
        "images/image3.jpg",
        text,
        "images/fontim.otf",
        190,
        (50, 50, 50),
        (1460, 1450),
        0,
    "images/saved/image3.png"
    )

def add_text_to_image_4(text):
    return add_text_to_image(
        "images/image4.jpg",
        text,
        "images/bold.ttf",
        250,
        (157, 139, 91),
        (1050, 1530),
        0,
        "images/saved/image4.png"
    )


from PIL import Image, ImageDraw, ImageFont

def add_text_to_image1(txt):
    image_path = "images/boyin.jpg"
    output_path = 'images/saved/boyin.png'
    img = Image.open(image_path)
    font_path = "images/Spring_Romance.otf"
    font_size = 30
    font_color = (255, 255, 255)  # White color
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(img)
    x, y = 50, 50
    draw.text((x, y), txt, fill=font_color, font=font)
    img.save(output_path)

    print(f"Text added to image and saved as {output_path}")
