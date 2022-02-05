import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Erosion and Dilation are known as morphological transformations. They are used to remove noise and small details from an image.

img = cv.imread("D:\\ImgData\\input\\balls.jpg", 0)
__, mask = cv.threshold(img, 230, 255, cv.THRESH_BINARY_INV)

#Erosion - It is used to erode boundaries of the foreground object.

#Kernel - It is a small sized matrix which will traverse through the image. It is used to remove noise and small details from an image.
kernel = np.ones((2,2), np.uint8)

erosion = cv.erode(mask, kernel)

#Dilation - It is used to dilate boundaries of the foreground object.
dilation = cv.dilate(mask, kernel)

#Opening - It perforns erosion followed by dilation over an image.
#Closing - It perforns dilation followed by erosion over an image.
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

#Tophat - It shows the difference between the input image and the opening of the image.
#Gradient - It shows the difference between the closing of the input image and opening of the input image.
#Blackhat - It shows the difference between the closing of the input image and the input image.
tophat = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel)
gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
blackhat = cv.morphologyEx(mask, cv.MORPH_BLACKHAT, kernel)


#Storing the images and corresponding titles in a list
titles = ['img', 'mask', 'erosion', 'dilation', 'opening', 'closing', 'tophat', 'grad', 'blackhat']
images = [img, mask, erosion, dilation, opening, closing, tophat, gradient, blackhat]

#Plotting the images and titles using matplotlib
for i in range(9):
    plt.subplot(3,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()

"""
cv.imshow("Image", blackhat)
cv.waitKey()
cv.destroyAllWimdows()
"""