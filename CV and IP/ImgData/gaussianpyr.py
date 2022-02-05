import cv2 as cv

#Gaussian Pyramid method is used to change the image resolution by half/ double. 


img = cv.imread("D:\\ImgData\\input\\img.jpg")
img = cv.resize(img, (480, 360))

#Here pyrDown() is used to reduce the resolution of the image by half, whereas pyrUp() is used to increase the resolution of the image by double.

pd1 = cv.pyrDown(img)
pd2 = cv.pyrDown(pd1)

#If we decrese the resolution of the image by half, then we can see that the image is blurred, due to Gaussian Pyramid.
#So reducing the resolution by half and again incresing it to double will not give us the original image, but a blurred image.
pu1 = cv.pyrUp(pd2)
pu2 = cv.pyrUp(pu1)

cv.imshow("Image", img)
cv.imshow("Image Down", pu2)


cv.waitKey()
cv.destroyAllWindows()