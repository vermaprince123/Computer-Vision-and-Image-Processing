import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


#Image thresholding is used to convert an image to a binary image. If a pixel value is greater than a threshold, it is converted to white, otherwise it is converted to black. Here, we have discussed simple as well as adaptive thresholding.
"""
img = cv.imread("D:\\ImgData\\input\\grad.jpg")

#threshold method takes four arguments:
#1. image
#2. threshold value
#3. maxVal
#4. threshold type

#Below are images for all the threshold types.
__, img1 = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
__, img2 = cv.threshold(img, 100, 255, cv.THRESH_BINARY_INV)
__, img3 = cv.threshold(img, 100, 255, cv.THRESH_TRUNC)
__, img4 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO)
__, img5 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO_INV)


titles = ['original', 'binary', 'binary_inv', 'trunc', 'to_zero', 'to_zero_inv']
images = [img, img1, img2, img3, img4, img5]

for i in range(6):
    plt.subplot(2,3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()

#cv.imshow("Image", img5)
#cv.waitKey()
#cv.destroyAllWindows
"""

#Adaptive Thresholding - This method is used to convert an image to binary image. It is useful when the image is not of uniform intensity.

img = cv.imread("D:\\ImgData\\input\\bw.png")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

__, img1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

#adaptiveThreshold method takes five arguments:
#1. image
#2. maxValue - This is the value that is assigned to the pixels for which the condition is satisfied.
#3. adaptiveMethod - ADAPTIVE_THRESH_MEAN_C or ADAPTIVE_THRESH_GAUSSIAN_C
#4. thresholdType (BINARY, BINARY_INV, TRUNC, TOZERO, TOZERO_INV)
#5. blockSize (must be odd)
#6. C - Constant subtracted from the mean or weighted mean.
img2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
img3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)


#Adding images and corresponding titles to a list and plotting them using matplotlib.
titles = ['original', 'binary', 'adap_mean', 'adap_gaussin']
images = [img, img1, img2, img3]

for i in range(4):
    plt.subplot(2,2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()

#cv.imshow("Image", img3)

#cv.waitKey()
#cv.destroyAllWindows()













