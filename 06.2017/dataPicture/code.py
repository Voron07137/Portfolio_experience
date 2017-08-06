from PIL import Image, ImageDraw
from datetime import datetime

text = "the Statue of Liberty, New York \n date and time: "
img = Image.open('Liberty.png').convert('RGBA')
imageDrawer = ImageDraw.Draw(img)
imageDrawer.text((180, 0), text, fill=(0, 0, 150, 200))
imageDrawer.text((270, 15), datetime.strftime(datetime.now(), "%d:%m:%Y %H:%M:%S"), fill=(0, 0, 150, 200))
img.save('Liberty_inscription_date.png')