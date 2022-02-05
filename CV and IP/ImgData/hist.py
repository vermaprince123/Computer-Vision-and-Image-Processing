import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread("D:\\ImgData\\input\\child.jpeg")
img = cv.resize(img, (300,300))
b, g, r = cv.split(img)

"""
#Plotting Histogram for different channels
#plt.hist(b.ravel(), 256, [0, 256])
#plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.title("BGR Histogram")
plt.show()


#Equalization of Histogram: - It is mainly used for enhancing the contrast of the image.
equal = cv.equalizeHist(img_gray)
#calcHist method takes five arguments:
#1. image
#2. number of channels - 0 for grayscale image and 1 for color image
#3. mask
#4. number of bins
#5. range of values
hist = cv.calcHist(equal, [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

cv.imshow("img", img_gray)
cv.imshow("eqimg", equal)
cv.waitKey()
cv.destroyAllWindows()
"""

#CLAHE - Contrast Limited Adaptive Histogram Equalization
#CLAHE is a histogram equalization technique that is also used to improve the contrast of an image.
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#This method takes two arguments:
#1. clipLimit - The contrast limit.
#2. tileGridSize - The size of the grid for histogram equalization.
clahe = cv.createCLAHE(clipLimit = 2.0, tileGridSize = (8,8))
#This method applies the CLAHE algorithm to the image.
cl = clahe.apply(img_gray)

hist = cv.calcHist(cl, [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

cv.imshow("img", img_gray)
cv.imshow("cl", cl)
cv.waitKey()
cv.destroyAllWindows()

