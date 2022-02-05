import cv2 as cv
import numpy as np

#HoughCircles method is used to detect circles in an image.
#It takes eight parameters:
#1. Input image
#2. Method to detect circles - cv.HOUGH_GRADIENT
#3. dp - Inverse ratio of the accumulator resolution to the image resolution.
#4. minDist - Minimum distance between the centers of the detected circles.
#5. param1 - First method-specific parameter. In case of cv.HOUGH_GRADIENT it is the higher threshold of the two passed to the cv.HoughLinesP function.
#6. param2 - Second method-specific parameter. In case of cv.HOUGH_GRADIENT it is the accumulator threshold at the center detection stage.
#7. minRadius - Minimum circle radius.
#8. maxRadius - Maximum circle radius.

"""
img = cv.imread("D:\\ImgData\\input\\balls.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_gray = cv.medianBlur(img_gray, 5)

#centre, radius
circles = cv.HoughCircles(img_gray, cv.HOUGH_GRADIENT, 1, 20, param1= 50, param2=40, minRadius=0, maxRadius=0)


data = np.uint16(np.around(circles))

for (x, y, r) in data[0, :]:
    cv.circle(img, (x,y), r, (255,0,255), 2)


cv.imshow("Image", img)

cv.waitKey()
cv.destroyAllWindows()
"""

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while True: 
    __, img = cap.read()
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_gray = cv.medianBlur(img_gray, 5)

    #centre, radius
    circles = cv.HoughCircles(img_gray, cv.HOUGH_GRADIENT, 1, 20, param1= 50, param2=40, minRadius=0, maxRadius=0)
    
    if circles is not None:
        data = np.uint16(np.around(circles))
        for (x, y, r) in data[0, :]:
            cv.circle(img, (x,y), r, (255,0,255), 2)


    cv.imshow("Image", img)
    
    if cv.waitKey(1) == 27:
        break
    

cap.release()
cv.destroyAllWindows()

    