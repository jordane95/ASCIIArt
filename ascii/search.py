# This file implements the search methods for some parameters
from ascii import preprocess_ascii, image_to_ascii, post_process
import cv2 as cv
import numpy as np

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
            # limit = image_to_ascii(hed, x0=288-6*17, y0=268-37*2, Tw=17, Th=37, Rw=24, Rh=5, letters=letters)
            # post process
            text = ''
            Rw = 24
            Rh = 5
            text_len = len(text)
            print("Processing the "+str(idx)+" th candidate, loss : %.2f" % loss)
            # post_process(limit, text, start=(Rw+1)*((Rh-1)//2)+(Rw-text_len)//2+1, save_path="results/limit.txt")
            post_process(whole, text, start=7*40+25, save_path="results/whole"+str(idx)+".txt")


if __name__ == '__main__':
    exhaustif_search(17, 37)
