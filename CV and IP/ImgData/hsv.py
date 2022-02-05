import cv2 as cv
import numpy as np

def cross(x):
    pass

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

#Create Trackbars for upper and lower hsv
cv.namedWindow("Trackbar")

cv.createTrackbar("l_h", "Trackbar", 0, 255, cross)
cv.createTrackbar("l_s", "Trackbar", 0, 255, cross)
cv.createTrackbar("l_v", "Trackbar", 0, 255, cross)

#Here initial values for upper HSV will be 255
cv.createTrackbar("u_h", "Trackbar", 255, 255, cross)
cv.createTrackbar("u_s", "Trackbar", 255, 255, cross)
cv.createTrackbar("u_v", "Trackbar", 255, 255, cross)

while True: 
    ret, img = cap.read()
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    l_h = cv.getTrackbarPos("l_h", "Trackbar")
    l_s = cv.getTrackbarPos("l_s", "Trackbar")
    l_v = cv.getTrackbarPos("l_v", "Trackbar")
    
    u_h = cv.getTrackbarPos("u_h", "Trackbar")
    u_s = cv.getTrackbarPos("u_s", "Trackbar")
    u_v = cv.getTrackbarPos("u_v", "Trackbar")
    
    l = np.array([l_h, l_s, l_v])
    u = np.array([u_h, u_s, u_v])
    
    #Create a mask
    mask = cv.inRange(hsv, l, u)

    #Apply mask using bitwise_and operator
    result = cv.bitwise_and(img, img, mask=mask)
    
    cv.imshow("Image", result)
    if cv.waitKey(1) == 27:
        break
    


cv.destroyAllWindows()