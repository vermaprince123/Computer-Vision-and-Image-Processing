import cv2 as cv
import numpy as np


#We have Harris as well as Shi-Tomasi method for detecting corners.

img = cv.imread("D:\\ImgData\\input\\shapes.jpg")
img = cv.resize(img, (500,390))

"""
#Harris
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_gray = np.float32(img_gray)

#This method takes four parameters:
#1. Image
#2. Block size - Size of neighbourhood considered for corner detection
#3. ksize - Aperture parameter of Sobel operator
#4. k - Harris detector free parameter in equation
c_d = cv.cornerHarris(img_gray, 7, 3, 0.04)

#We need to normalize the cornerness values to range [0, 255]
img[c_d>0.01*c_d.max()] = [0,0,0]

"""

#Shi-Tomasi method

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#This method takes four parameters:
#1. Image
#2. Max number of corners to be returned
#3. Quality level - minimal accepted quality of corners
#4. Min distance between corners
corner = cv.goodFeaturesToTrack(img_gray, 1000, 0.01, 50)

#We need to convert the corner coordinates to int
corner = np.int64(corner)

for i in corner:
    #Flatten the array
    x,y = i.ravel()
    cv.circle(img, (x,y), 4, (255,100,255), -1)

cv.imshow("image", img)
cv.waitKey()
cv.destroyAllWindows()