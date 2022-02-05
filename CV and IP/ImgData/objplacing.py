import cv2 as cv
import numpy as np

img1 = cv.imread("D:\\ImgData\\input\\fruit.png")
img2 = cv.imread("D:\\ImgData\\input\\apple.jpg")

img1 = cv.resize(img1, (960,540))
img2 = cv.resize(img2, (450,450))


r,c,ch = img2.shape
roi = img1[0:r, 0:c]

img2_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
__, mask = cv.threshold(img2_gray, 215, 255, cv.THRESH_BINARY_INV)

#Getting foreground of second image
img2_fg = cv.bitwise_and(img2, img2, mask=mask)
#Getting background of first image
mask_inv = cv.bitwise_not(mask)
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

#Adding foreground and background
res = cv.add(img1_bg, img2_fg)

#Merging both images
merged = img1
merged[0:r, 0:c] = res

cv.imshow("Img1", img1)
cv.imshow("Img2", merged)



cv.waitKey()
cv.destroyAllWindows()