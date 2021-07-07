# test the fonctions of ascii module
from ascii import preprocess_ascii, image_to_ascii, post_process
import cv2 as cv
import numpy as np

def draw_patch(image, x0, y0, Tw, Th, Rw, Rh):
    image = np.asarray(image)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    for i in range(Rw):
        for j in range(Rh):
            start_point = (x0+i*Tw, y0+j*Th)
            end_point = (x0+(i+1)*Tw, y0+(j+1)*Th)
            image = cv.rectangle(image, start_point, end_point, (0, 0, 255))
    cv.imwrite("images/hed_patch.jpg", image)
    cv.imshow("Patches", image)
    cv.waitKey(0)
    return None

letters = preprocess_ascii(Tw=8, Th=18, more_char=False)

hed = cv.imread("./images/masked_hed.jpg")
hed = cv.cvtColor(hed, cv.COLOR_BGR2GRAY)

result, loss = image_to_ascii(hed, x0=288-6*17, y0=268-37, Tw=8, Th=18, Rw=16, Rh=6, letters=letters)

draw_patch(hed, x0=288-6*17, y0=268-37, Tw=8, Th=18, Rw=16, Rh=6)

post_process(result, None, 0, save_path='triangle.txt')
