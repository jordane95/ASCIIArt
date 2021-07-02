from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt
from skimage import morphology

def preprocess_ascii(Tw=15, Th=28, font_size=24, ratio=0.9, more_char=True):
    font = ImageFont.truetype('fonts/Menlo.ttc', size=font_size)
    letters = {}
    xx = list(range(32, 127))
    if more_char:
        xx.extend(
            [915, 956, 1084, 1085, 1096, 8213, 8242, 8712, 8736, 8743, 8746, 8747, 8765, 8978, 9472, 9474, 9484, 9488, 9496,
             9500, 9508, 9524, 9581, 9582, 9583, 9584, 9585, 9586, 9621, 9651])

    for i in xx:
        img = Image.new("RGB", (15, 28), "white")
        d = ImageDraw.Draw(img)
        d.text((0, 0), chr(i), font=font, fill='black')
        # img = ndimage.gaussian_filter(img, 1))
        img = img.resize((Tw, Th))
        plt.figure(chr(i))
        plt.imshow(img)
        plt.show()
        print(np.asarray(img).shape)
        img_data = np.asarray(img)
        letters[i] = img
    return letters

if __name__ == "__main__":
    preprocess_ascii()

