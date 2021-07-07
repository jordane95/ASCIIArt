# This file implements the search methods for some parameters
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
    cv.imwrite("images/canny_patch.jpg", image)
    # cv.imshow("Patches", image)
    # cv.waitKey(0)
    return None


def exhaustif_search(Tw, Th):
    # serach all the position of segmentation space, find the best one
    # preparation
    letters = preprocess_ascii(more_char=True)
    hed = cv.imread("images/masked_hed.jpg")
    hed = cv.cvtColor(hed, cv.COLOR_BGR2GRAY)
    H, W = hed.shape
    # exhaustif search
    idx = 0
    for x0 in range(0, Tw, 4):
        for y0 in range(0, Th, 4):
            idx += 1
            # ascii matching
            whole, loss = image_to_ascii(hed, x0=x0, y0=y0, Tw=17, Th=37, Rw=W//Tw-1, Rh=H//Th-1, letters=letters)
            limit, loss_lim = image_to_ascii(hed, x0=288-6*17+x0, y0=268-37*2+y0, Tw=17, Th=37, Rw=24, Rh=5, letters=letters)
            if idx == 1: draw_patch(hed, x0=288-6*17+x0, y0=268-37*2+y0, Tw=17, Th=37, Rw=24, Rh=5)
            # post process
            text = ''
            Rw = 24
            Rh = 5
            text_len = len(text)
            print("Processing the "+str(idx)+" th candidate, loss : %.2f" % loss)
            post_process(limit, text, start=(Rw+1)*((Rh-1)//2)+(Rw-text_len)//2+1, save_path="results/limit"+str(idx)+".txt")
            print("Processing the "+str(idx)+" th candidate, loss : %.2f" % loss_lim)
            post_process(whole, text, start=7*40+25, save_path="results/whole"+str(idx)+".txt")


if __name__ == '__main__':
    exhaustif_search(17, 37)
