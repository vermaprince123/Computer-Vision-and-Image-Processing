import cv2 as cv

img1 = cv.imread("D:\\ImgData\\input\\th.png")
img2 = cv.imread("D:\\ImgData\\input\\th2.png")

#Add Border
img1 = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=[255, 0, 255])
#This function takes four parameters:
#src: Input image.
#top, bottom, left and right: Number of pixels in each direction. These parameters can be negative.
#borderType: Type of the border. You can check out the documentation for more details on border types
#value: Color value of the border.

#Adding Images
img = cv.add(img1, 0.8, img2, 0.2, 0)
#This function takes five parameters:
#src1: First input image.
#alpha: Weight of the first image.
#src2: Second input image.
#beta: Weight of the second image.
#dst: Output image.
#But we generally use addweighted function to blend images over add.

#Blending Images
img = cv.addWeighted(img1, 0.8, img2, 0.2, 0)
#This function also takes five parameters, same as given in the previous function.

img = cv.resize(img, (640,360))

cv.imshow("Image", img)

cv.waitKey()
cv.destroyAllWindows()