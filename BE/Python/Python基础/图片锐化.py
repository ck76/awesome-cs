import cv2 as cv
import numpy as np


def custom_blur_demo(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 锐化
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imshow("demo", dst)
    cv.imwrite("123.png",dst)


src = cv.imread("1.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
custom_blur_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()