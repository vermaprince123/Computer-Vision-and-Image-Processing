import cv2 as cv
import numpy as np


#Template matching is a method to find the location of a small part of image in the same image.


img = cv.imread("D:\\ImgData\\input\\img.jpg")
temp = cv.imread("D:\\ImgData\\input\\temp.jpg", 0)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Switching of rows and columns
w, h = temp.shape[::-1]

#matchTemplate() function takes the image and template as input and returns the location of the template in the image.
#Here as the method is TM_CCORR_NORMED, the pixel values matching the template will be brightest/ of maximum intensity in the result image.
result = cv.matchTemplate(img_gray, temp, cv.TM_CCORR_NORMED)

#Limiting the result to a threshold value to get the brightest pixel values.
lim = 0.997
brpx = np.where(result>=lim)

count = 0
#Zipping the matrix and interchanging rows and columns of the brightest pixel values.
#Here i is the array having x and y coordinates of the brightest pixel values.
for i in zip(*brpx[::-1]):
    cv.rectangle(img, i, (i[0]+w, i[1]+h), (255,255,255), 2)
    count+=1
#To count number of brightest pixel values exceeding the threshold value. We must manually increase the 'lim' value until we don't get more than one result.
print(count)
img = cv.resize(img, (480, 360))
result = cv.resize(result, (480, 360))
cv.imshow("Image", img)
cv.waitKey()
cv.destroyAllWindows()