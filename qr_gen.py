import qrcode
from PIL import ImageDraw, ImageFont


box_size = 100
url = "https://github.com/phoughton"
img = qrcode.make(url,
                  box_size=box_size,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  border=1)

file_path = "github_qr_code.png"
# img.save(file_path)

draw = ImageDraw.Draw(img)
text = "Pete Houghton"

font = ImageFont.truetype("DejaVuSans.ttf", box_size*3.5)
left, top, right, bottom = font.getbbox(text)

text_height = abs(bottom - top)
text_width = abs(right - left)

x = (img.size[1] - text_width) / 2
y = (img.size[0] - text_height) / 2
draw.rectangle((x, y,
                x + int(text_width*1.2),
                y + int(text_height*1.2)),
                fill="white")

draw.text((x, y), text, font=font)

img.save(file_path)
