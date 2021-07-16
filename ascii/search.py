# This file implements the search methods for some parameters
from ascii import preprocess_ascii, image_to_ascii, post_process
import cv2 as cv
import numpy as np
import os


def draw_patch(image, x0, y0, Tw, Th, Rw, Rh, idx):
    image = np.asarray(image)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    for i in range(Rw):
        for j in range(Rh):
            start_point = (x0+i*Tw, y0+j*Th)
            end_point = (x0+(i+1)*Tw, y0+(j+1)*Th)
            image = cv.rectangle(image, start_point, end_point, (0, 0, 255))
    save_path = "./patches/"
    if not os.path.exists(save_path): os.mkdir(save_path)
    cv.imwrite(save_path+"patch_"+str(idx)+".jpg", image)
    # cv.imshow("Patches", image)
    # cv.waitKey(0)
    return None


def exhaustif_search(Tw=15, Th=28):
    # serach all the position of segmentation space, find the best one
    # preparation
    save_path = "./results/"
    if not os.path.exists(save_path): os.mkdir(save_path)
    letters = preprocess_ascii(Tw=Tw, Th=Th, more_char=True)
    hed = cv.imread("../images/masked_hed.jpg")
    hed = cv.cvtColor(hed, cv.COLOR_BGR2GRAY)
    H, W = hed.shape
    # exhaustif search
    idx = 0
    for x0 in range(0, Tw, Tw//7):
        for y0 in range(0, Th, Th//7):
            idx += 1
            # ascii matching
            whole, loss = image_to_ascii(hed, x0=x0, y0=y0, Tw=Tw, Th=Th, Rw=W//Tw-1, Rh=H//Th-1, letters=letters)
            draw_patch(hed, x0=x0, y0=y0, Tw=Tw, Th=Th, Rw=W//Tw-1, Rh=H//Th-1, idx=idx)
            # post process
            text = ''
            print("Processing the "+str(idx)+" th candidate, loss : %.2f" % loss)
            post_process(whole, text, start=7*40+25, save_path="./results/whole"+str(idx)+".txt")


if __name__ == '__main__':
    exhaustif_search(17, 37)
