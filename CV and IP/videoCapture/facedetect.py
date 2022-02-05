import cv2 as cv
import numpy as np

#Loading Haar Cascade file for face and eye detection
face = cv.CascadeClassifier("D:\\ImgData\\input\\haarcascade_frontalface_default.xml")
eye = cv.CascadeClassifier("D:\\ImgData\\input\\haarcascade_eye.xml")

def detector(img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #detection of face
    faces = face.detectMultiScale(img_gray, 1.3, 4)
    

    for (fx, fy, fw, fh) in faces:
        cv.rectangle(img, (fx, fy), (fx+fw, fy+fh), (100, 255, 100), 5)
        
        roi = img[fy:fy+fh, fx:fx+fw]
        roi_gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)

        #Detection of eyes inside face
        eyes = eye.detectMultiScale(roi_gray, 1.3, 4)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi, (ex, ey), (ex+ew, ey+eh), (200, 100, 200), 5)
        
    return img

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    __, frame = cap.read()
    
    frame = detector(frame)
    
    cv.imshow("face detect", frame)
    
    if cv.waitKey(1) == 27:
        break
    

cap.release()
cv.destroyAllWindows()