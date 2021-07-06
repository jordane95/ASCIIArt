import cv2 as cv
from PIL import Image, ImageDraw, ImageFont

class Tone:
    def __init__(image_path='images/hed.jpg', Rw, Rh, font_path="fonts/Menlo.ttc"):
        image = cv.imread(image_path)
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        font = ImageFont.truetype(font_path, size=12)
        Tw, Th = font.getsize('a')
        ascii_enc = ""
        

image = cv.imread("images/hed.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# image.resize((100, 150))
print(image.aspect_ratio)
cv.imshow("Subsampled", image)
cv.waitKey(0)

pixel_to_ascii = "$#@&%ZYXWVUTSRQPONMLKJIHGFEDCBA098765432?][}{/)(><zyxwvutsrqponmlkjihgfedcba*+1-."

text = ""
for l in image:
    for p in l:
        label = round(p / 255 * (len(pixel_to_ascii)-1))
        text += p2t[label]
    text += '\n'
fp = open("tone.txt", 'w', encoding='utf8')
fp.write(text)
fp.close()
