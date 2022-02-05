import cv2 as cv
import numpy as np

img = cv.imread("D:\\ImgData\\input\\th.png")
img = cv.resize(img, (640,360))


px = img[300,500]

#Here 0 corresponds to Blue, 1 to Green and 2 to Red
bpx = img[300,500,0]
gpx = img[300,500,1]
rpx = img[300,500,2]
print(px)
print("Blue - ", bpx)
print("Green - ", gpx)
print("Red - ", rpx)

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()