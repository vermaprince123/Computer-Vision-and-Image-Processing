import cv2 as cv
import numpy as np

def do_nothing(x):
    pass

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars", (300,300))

#trackbars --> mask --> thresh --> contours -->hull

#create trackbars
cv.createTrackbar("Thresh", "Trackbars", 0, 255, do_nothing)

cv.createTrackbar("L_H", "Trackbars", 0, 255, do_nothing)
cv.createTrackbar("L_S", "Trackbars", 0, 255, do_nothing)
cv.createTrackbar("L_V", "Trackbars", 0, 255, do_nothing)

cv.createTrackbar("U_H", "Trackbars", 255, 255, do_nothing)
cv.createTrackbar("U_S", "Trackbars", 255, 255, do_nothing)
cv.createTrackbar("U_V", "Trackbars", 255, 255, do_nothing)

while True:
    __, frame = cap.read()
    frame = cv.resize(frame, (300,300))
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    
    #get the trackbar position
    l_h = cv.getTrackbarPos("L_H", "Trackbars")
    l_s = cv.getTrackbarPos("L_S", "Trackbars")
    l_v = cv.getTrackbarPos("L_V", "Trackbars")
    
    u_h = cv.getTrackbarPos("U_H", "Trackbars")
    u_s = cv.getTrackbarPos("U_S", "Trackbars")
    u_v = cv.getTrackbarPos("U_V", "Trackbars")
    
    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])
    
    mask = cv.inRange(hsv, lower, upper)
    fil = cv.bitwise_and(frame, frame, mask=mask)
    
    #get thresh limit
    th = cv.getTrackbarPos("Thresh", "Trackbars")
    
    #create threshold
    ret, thresh = cv.threshold(mask,th,255,cv.THRESH_BINARY)
    thresh = cv.dilate(thresh, (5,5), iterations=2)
    
    cnts, heir = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:
        epsilon = 0.0001*cv.arcLength(c, True)
        data = cv.approxPolyDP(c, epsilon, True)
        
        hull = cv.convexHull(data)
        
        cv.drawContours(frame, [c], -1, (0,0,255), 2)
        cv.drawContours(frame, [hull], -1, (0,255,0), 2)
    
    cv.imshow("Frame", frame)
    cv.imshow("Filter", fil)
    cv.imshow("Mask", mask)
    
    if cv.waitKey(1) == 27:
        break 

        
cap.release()
cv.destroyAllWindows()
