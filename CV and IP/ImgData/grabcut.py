import cv2 as cv
import numpy as np

img = cv.imread("D:\\ImgData\\input\\hand.jpg")


#mask
mask = np.zeros(img.shape[:2], np.uint8)
#rect
rect = (6,31,360,527)
# Creating bgModel fgModel
bgModel = np.zeros((1,65), np.float64)*255
fgModel = np.zeros((1,65), np.float64)*255

cv.grabCut(img, mask, rect, bgModel, fgModel, 5, cv.GC_INIT_WITH_RECT)
#sure bg 0
#sure fg 1
#partial bg 2
#partial fg 3


#Creating a mask for partial and sure background
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

cv.imshow("image", img)

cv.waitKey()
cv.destroyAllWindows()