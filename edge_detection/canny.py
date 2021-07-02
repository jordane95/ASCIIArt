import cv2 as cv

image = cv.imread('images/input.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5, 5), 0)
canny = cv.Canny(blurred, 30, 150)
canny_coarse = cv.Canny(blurred, 150, 250)

# print(image.shape)
# print(canny.shape)
cv.imwrite('images/canny.jpg', canny)
cv.imwrite('images/canny_coarse.jpg', canny_coarse)

cv.imshow('Input', image)
cv.imshow('Canny', canny)
cv.imshow('CannyCoarse', canny_coarse)

cv.waitKey(0)

