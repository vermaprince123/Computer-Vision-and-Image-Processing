import cv2 as cv

img1 = cv.imread("D:\\ImgData\\input\\th1.png")
img1 = cv.resize(img1, (640,360))

img2 = cv.imread("D:\\ImgData\\input\\th2.png")
img2 = cv.resize(img2, (640,360))

#(443,159) -- (584,296)
roi = img1[159:296, 443:584]
#428, 159
img2[159:296, 428:569] = roi


cv.imshow("Image", img2)

cv.waitKey()
cv.destroyAllWindows()