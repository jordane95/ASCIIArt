# This program will simulate the overall pipeline of the system
from edge_detection.hed import hed
import cv2 as cv

structure_map = hed()
# structure_map = cv.cvtColor(structure_map, cv.COLOR_BGR2GRAY)

cv.imshow("S", structure_map)
cv.waitKey(0)
