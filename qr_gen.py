import qrcode
from PIL import ImageDraw, ImageFont


url = "https://github.com/phoughton"
img = qrcode.make(url, box_size=10, border=2)

file_path = "github_qr_code.png"
# img.save(file_path)

draw = ImageDraw.Draw(img)
text = "Pete Houghton"

font = ImageFont.truetype("DejaVuSans.ttf", 40)
left, top, right, bottom = font.getbbox(text)

text_height = abs(bottom - top)
text_width = abs(right - left)
# print(text_height, text_width)
print(img.size[0], img.size[1])
x = (img.size[1] - text_width) / 2
y = (img.size[0] - text_height) / 2
# print(x, y)
draw.text((x, y), text, font=font)

img.save(file_path)
