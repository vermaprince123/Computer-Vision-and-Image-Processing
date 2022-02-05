import cv2 as cv

img = cv.imread("D:\\ImgData\\input\\edilogo.jpg")
img = cv.resize(img, (320,320))

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
__, th1 = cv.threshold(img_gray, 250, 255, cv.THRESH_BINARY_INV)

#findCountours method takes 3 arguments. First one is source image, second is contour retrieval mode, third is contour approximation method
cnt, heir = cv.findContours(th1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#The function returns two values. First one is the list of contours(array of x and y cordinates) and the second one is hierarchy(image information).

#Used to draw countours. First argument is source image, second is contour, third is color, fourth is thickness
img1 = cv.drawContours(img, cnt, -1, (200,100,200), 3)

print(cnt)
print(len(cnt))
print(heir)

cv.imshow("Img", img1)
cv.waitKey()
cv.destroyAllWindows()