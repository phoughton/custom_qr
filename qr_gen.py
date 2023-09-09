import qrcode
from PIL import ImageDraw, ImageFont
import argparse

parser = argparse.ArgumentParser(description='Generate a QR code with a logo')
parser.add_argument('-e', '--encoded_text',
                    help='Text to encode',
                    required=True)
parser.add_argument('-v', '--visible_text',
                    help='Text to overlay',
                    required=True)
parser.add_argument('-o', '--output_file',
                    help='Output PNG file',
                    required=True)
args = parser.parse_args()

box_size = 100
img = qrcode.make(args.encoded_text,
                  box_size=box_size,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  border=1)

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("DejaVuSans.ttf", box_size*3.5)
left, top, right, bottom = font.getbbox(args.visible_text)

text_height = abs(bottom - top)
text_width = abs(right - left)

x = (img.size[1] - text_width) / 2
y = (img.size[0] - text_height) / 2
draw.rectangle((x, y,
                x + int(text_width*1.2),
                y + int(text_height*1.2)),
                fill="white")

draw.text((x, y), args.visible_text, font=font)

img.save(args.output_file)
