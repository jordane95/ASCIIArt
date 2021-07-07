import numpy as np
import cv2 as cv

def get_bounds(boxes, W, H):
    x_min, x_max, y_min, y_max = W, 0, H, 0
    for box in boxes:
        for point in box:
            if point[0]<x_min: x_min = point[0]
            if point[0]>x_max: x_max = point[0]
            if point[1]<y_min: y_min = point[1]
            if point[1]>y_max: y_max = point[1]
    w, h = x_max-x_min, y_max-y_min
    x_left = int(max(0, x_min-w//2))
    x_right = int(min(x_max+w//2, W))
    y_top = int(max(0, y_min-3*h))
    y_bottom = int(min(H, y_max+3*h))
    return x_left, x_right, y_top, y_bottom

def segment(image, text_box, text_len, max_grid=140):
    image = np.asarray(image)
    xs = np.array(text_box)[:, 0]
    ys = np.array(text_box)[:, 1]
    x_min, x_max, y_min, y_max = min(xs), max(xs), min(ys), max(ys)
    # assume the text is single line
    # compute grid size
    # print(x_min, x_max, y_min, y_max, text_len)
    Th = round(y_max-y_min)
    Tw = round((x_max-x_min)/text_len)
    # segment the image into patches starting from text box
    Rw = 2*text_len
    Rh = 5
    return Tw, Th, Rw, Rh

def draw_patch(image, x0, y0, Tw, Th, Rw, Rh):
    image = np.asarray(image)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    for i in range(Rw):
        for j in range(Rh):
            start_point = (x0+i*Tw, y0+j*Th)
            end_point = (x0+(i+1)*Tw, y0+(j+1)*Th)
            image = cv.rectangle(image, start_point, end_point, (0, 0, 255))
    cv.imwrite("images/canny_patch.jpg", image)
    cv.imshow("Patches", image)
    cv.waitKey(0)
    return None

def mask(image, box):
    image = np.asarray(image)
    xs = np.array(box)[:, 0]
    ys = np.array(box)[:, 1]
    x_min, x_max, y_min, y_max = round(min(xs)), round(max(xs)), round(min(ys)), round(max(ys))
    print(x_max, x_min)
    print(image.shape)
    image[y_min:y_max, x_min:x_max] = np.zeros((y_max-y_min, x_max-x_min, 3))
    return image
