import cv2 as cv

def canny(img_path='images/input.jpg', save_path='images/'):
    image = cv.imread(img_path)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    canny = cv.Canny(blurred, 30, 150)
    canny_coarse = cv.Canny(blurred, 150, 250)

    # print(image.shape)
    # print(canny.shape)
    cv.imwrite(save_path+'canny.jpg', canny)
    cv.imwrite(save_path+'canny_coarse.jpg', canny_coarse)

    # cv.imshow('Input', image)
    # cv.imshow('Canny', canny)
    # cv.imshow('CannyCoarse', canny_coarse)

    reversed_canny = 255-canny
    cv.imwrite(save_path+'rev_canny.jpg', reversed_canny)

    reversed_canny_coarse = 255-canny_coarse
    cv.imwrite(save_path+'rev_canny_coarse.jpg', reversed_canny_coarse)

    # cv.waitKey(0)

if __name__=="__main__":
    canny(img_path='images/africa.jpg')