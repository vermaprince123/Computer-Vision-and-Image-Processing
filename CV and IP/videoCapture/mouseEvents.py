import cv2 as cv
import numpy as np

"""
def drawCircle(event, x,y, flags, params):
    print(str(x)+" , "+str(y))
    print(event)
    print(flags)
    if event==cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x,y),50,(100,100,255),5)
    if event==cv.EVENT_RBUTTONDBLCLK:
        cv.circle(img, (x,y),50,(255,100,100),5)
    
"""

def printValues(event, x,y, flags, params):
    font = cv.FONT_HERSHEY_COMPLEX

    #Detection of the mouse event
    if event==cv.EVENT_LBUTTONDBLCLK:
        #Putting (x,y) coordinates on left button click
        text = ". - ("+str(x)+" , "+str(y)+")"
        cv.putText(img, text, (x,y), font, 0.5, (100,200,255))
    if event==cv.EVENT_RBUTTONDBLCLK:
        #Putting bgr values on right button click
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]
        text = ". ("+str(r)+" , "+str(g)+" , "+str(b)+")"
        cv.putText(img, text, (x,y), font, 0.5, (200,100,255))

cv.namedWindow(winname ="draw")
img = cv.imread("D:\\videoCapture\\img.jpg")

#Binding mouse events to the window
#setMouseCallback takes 2 arguments:
#1. window name
#2. callback function
cv.setMouseCallback("draw", printValues)

#Detecting and Updating the window on mouse click event
while True:
    cv.imshow("draw", img)
    if cv.waitKey(1)==ord('q'):
        break


cv.destroyAllWindows()