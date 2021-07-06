# test the fonctions of ascii module
from ascii import preprocess_ascii, image_to_ascii, post_process
import cv2 as cv

letters = preprocess_ascii(Tw=15, Th=18, more_char=False)

hed = cv.imread("./images/masked_hed.jpg")
hed = cv.cvtColor(hed, cv.COLOR_BGR2GRAY)

result, loss = image_to_ascii(hed, x0=288-6*17, y0=268-37, Tw=15, Th=18, Rw=5, Rh=6, letters=letters)

post_process(result, None, 0, save_path='triangle.txt')

cv.imshow("Masked HED", hed)
cv.waitKey(0)
