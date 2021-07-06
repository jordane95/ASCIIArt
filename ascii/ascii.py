from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2 as cv
from metrics import SAD

def preprocess_ascii(Tw=17, Th=37, font_size=24, mode="L", more_char=True):
    font = ImageFont.truetype('fonts/Menlo.ttc', size=font_size)
    letters = {}
    xx = list(range(32, 127))
    if more_char:
        xx.extend(
            [915, 956, 1084, 1085, 1096, 8213, 8242, 8712, 8736, 8743, 8746, 8747, 8765, 8978, 9472, 9474, 9484, 9488, 9496,
             9500, 9508, 9524, 9581, 9582, 9583, 9584, 9585, 9586, 9621, 9651])

    for i in xx:
        img = Image.new(mode, (15, 28), "black")
        d = ImageDraw.Draw(img)
        d.text((0, 0), chr(i), font=font, fill='white')
        # img = ndimage.gaussian_filter(img, 1))
        img = img.resize((Tw, Th))
        # plt.figure(chr(i))
        # plt.imshow(img)
        # plt.show()
        # print(np.asarray(img))
        img_data = np.asarray(img)
        # print(img_data.shape)
        # print(img_data)
        letters[i] = img_data
    # letters.pop(64)
    # letters.pop(37)
    return letters

def image_to_ascii(image, x0, y0, Tw, Th, Rw, Rh, letters):
    # print(image.shape)
    # for line in image:
    #     print(line)
    def argmin(d):
        if not d: return None
        min_val = min(d.values())
        return [k for k in d if d[k] == min_val][0]
    
    result = ""
    loss = 0
    for i in range(Rh):
        for j in range(Rw):
            # print("position: i = %d, j = %d" % (i, j))
            # get the current patch of the image
            patch = image[y0+i*Th:y0+(i+1)*Th, x0+j*Tw:x0+(j+1)*Tw]
            # print("Patch: \n", patch)
            distances = {l:SAD(patch, letters[l]) for l in letters}
            # print(distances)
            best_match = argmin(distances)
            result += chr(best_match)
            loss += distances[best_match]
        result += "\n"
    result = result[:-1]
    loss /= (Rw*Rh)
    return result, loss

def post_process(result, text, start, save_path="result.txt"):
    if text:
        # replace the corrsponding location with text from OCR
        end = start+len(text)
        result = result[:start]+text+result[end:]
    # save the result in result.txt
    fp = open(save_path, 'w', encoding='utf8')
    fp.write(result)
    fp.close()
    return result

if __name__ == "__main__":
    # pre process
    letters = preprocess_ascii(more_char=False)
    canny = cv.imread("images/hed.jpg")
    canny = cv.cvtColor(canny, cv.COLOR_BGR2GRAY)
    # ascii matching
    whole = image_to_ascii(canny, x0=0, y0=0, Tw=17, Th=37, Rw=40, Rh=12, letters=letters)
    limit = image_to_ascii(canny, x0=288-6*17, y0=268-37*2, Tw=17, Th=37, Rw=24, Rh=5, letters=letters)
    # post process
    text = 'PSYANGJI.COM'
    Rw = 24
    Rh = 5
    text_len = len(text)
    post_process(limit, text, start=(Rw+1)*((Rh-1)//2)+(Rw-text_len)//2+1, save_path="results/limit.txt")
    post_process(whole, text, start=7*40+25, save_path="results/whole.txt")

