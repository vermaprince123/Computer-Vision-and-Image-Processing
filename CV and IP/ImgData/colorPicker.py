import cv2 as cv
import numpy as np

#Callback function
def cross(x):
    pass

#Creating a black image using numpy array of 800x600 dimensions and three channels.
img = np.zeros((800,600,3), np.uint8)
#Creating a named window
cv.namedWindow("Color Picker")

#Creating an ON/OFF switch for the color picker
cv.createTrackbar("ON/OFF","Color Picker", 0,1, cross)

#createTrackar takes five arguments:
#1. name of the trackbar
#2. name of the window
#3. initial value of the trackbar
#4. max value of the trackbar
#5. callback function

#Creating trackars for Red, Green and Blue color components.
cv.createTrackbar("Red","Color Picker", 0,255, cross)
cv.createTrackbar("Green","Color Picker", 0,255, cross)
cv.createTrackbar("Blue","Color Picker", 0,255, cross)

#Setting a while loop to update the trackbar change in the image
while True:
    cv.imshow("Color Picker", img)
    if cv.waitKey(1)==27:
        break
    
    #Getting the value of the trackbar
    #getTrackbarPos takes two arguments:
    #1. name of the trackbar
    #2. name of the window
    s = cv.getTrackbarPos("ON/OFF", "Color Picker")
    r = cv.getTrackbarPos("Red", "Color Picker")
    g = cv.getTrackbarPos("Green", "Color Picker")
    b = cv.getTrackbarPos("Blue", "Color Picker")
    
    if s==0:
        img[:] = 0
    else:
        #Setting the color of the image
        img[:] = [b,g,r]
        

cv.destroyAllWindows()