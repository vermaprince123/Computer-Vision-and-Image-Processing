import cv2 as cv
import numpy as np

#img = cv.imread("D:\\ImgData\\input\\childimg.jpeg")
img = np.ones([600,800,3], np.uint8)*200
img = cv.resize(img, (800,600))

#Line - > img, start, end, color, thickness
img = cv.line(img, (0,0), (400,400), (2,188,250), 5)
img = cv.arrowedLine(img, (200,300), (400,500), (25,180,25), 10)

#Rect --> img, start, end, color, thickness
img = cv.rectangle(img, (400,100), (300,400), (67,67,200), 2)

#Circle --> img, center, radius, thickness
img = cv.circle(img, (500,300), 50, (200,67,67), 6)

#Elipse -->img,start,l-w, or, degree, color, th
img = cv.ellipse(img, (500,400), (100,50), 90,45,300,(100,100,100), 7)

#putText --> img,text,start,style,size,color, thickness
font = cv.FONT_HERSHEY_SCRIPT_COMPLEX
img = cv.putText(img, "Edignite NGO", (400,200), font, 2, (240,120,120), 5, cv.LINE_AA)

cv.imshow("Img", img)

cv.waitKey(0)
cv.destroyAllWindows()