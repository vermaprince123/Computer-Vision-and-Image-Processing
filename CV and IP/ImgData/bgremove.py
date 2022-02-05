import cv2 as cv

img = cv.imread("D:\\ImgData\\input\\orange.png")
img = cv.resize(img, (300,300))

#convert to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#reading background pixels and converting to hsv
roi = cv.imread("D:\\ImgData\\input\\orangebg.png")
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

#defining the lower and upper range of the background
hist_roi = cv.calcHist([hsv_roi], [0,1], None, [180,256], [0, 180, 0, 256])
mask = cv.calcBackProject([hsv], [0,1], hist_roi, [0, 180, 0, 256], 1)

#applying the mask
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
mask = cv.filter2D(mask, -1, kernel)
__, mask = cv.threshold(mask, 210, 255, cv.THRESH_BINARY)

#merging mask into an image
mask = cv.merge((mask, mask, mask))
#result image
result = cv.bitwise_or(img, mask)



cv.imshow("Image", img)
cv.imshow("Mask", mask)
cv.imshow("HSV", result)



cv.waitKey()
cv.destroyAllWindows()