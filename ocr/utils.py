import numpy as np

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

