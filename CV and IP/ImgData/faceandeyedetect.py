import cv2 as cv
import numpy as np

face = cv.CascadeClassifier("D:\\ImgData\\input\\haarcascade_frontalface_default.xml")
eye = cv.CascadeClassifier("D:\\ImgData\\input\\haarcascade_eye.xml")

img = cv.imread("D:\\ImgData\\input\\img.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face.detectMultiScale(img_gray, 1.2, 4)

for (x, y, w, h) in faces:
    img = cv.rectangle(img, (x,y), (x+w, y+h), (0,200,200), 5)
    
    roi = img[y:y+h, x:x+w]
    roi_gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    eyes = eye.detectMultiScale(roi_gray, 1.5, 2)
    
    for (x1, y1, w1, h1) in eyes:
        cv.rectangle(roi, (x1, y1), (x1+w1, y1+h1), (200,200,10), 2)


img = cv.resize(img, (480, 360))
cv.imshow("Face Detected", img)
cv.waitKey()
cv.destroyAllWindows()