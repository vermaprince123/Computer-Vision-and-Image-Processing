import cv2 as cv
import numpy as np

#Hough Transform is a way to detect straight lines/ shape in an image.

img = cv.imread("D:\\ImgData\\input\\bricks.png")

#Converting image to gray scale and detecting edges using Canny edge detection
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(img_gray, 10, 200, apertureSize = 3)

#r,theta --> r = xcos(theta) + ysin(theta)
"""
#HoughLines method takes three arguments:
#1. Input image
#2. rho: Distance resolution of the accumulator in pixels.
#3. theta: Angle resolution of the accumulator in radians.
lines = cv.HoughLines(edges, 1, np.pi/180, 100)

for rho, theta in lines[0]:
    c = np.cos(theta)
    s = np.sin(theta)
    

    x0 = rho*c
    y0 = rho*s


    #Finding the end points of the line
    x1 = int(x0 + 1000*(-s))
    y1 = int(y0 + 1000*(c))
    x2 = int(x0 - 1000*(-s))
    y2 = int(y0 - 1000*(c))
    
    #Plotting lines
    cv.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

"""

#HoughLinesP - > x1, y1, x2, y2

#HoughLinesP method takes six arguments:
#1. Input image
#2. rho: Distance resolution of the accumulator in pixels.
#3. theta: Angle resolution of the accumulator in radians.
#4. threshold: Accumulator threshold parameter. Only those lines are returned that get enough votes ( > threshold).
#5. minLineLength: Minimum line length. Line segments shorter than that are rejected.
#6. maxLineGap: Maximum allowed gap between points on the same line to link them.
lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength = 5, maxLineGap=150)


for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv.imshow("Image", img)
cv.imshow("Edges", edges)


cv.waitKey()
cv.destroyAllWindows()