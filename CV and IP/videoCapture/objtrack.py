import cv2 as cv
import numpy as np

cap = cv.VideoCapture("D:\\VideoCapture\\videos\\test.mp4")

#Reading the first frame
ret, frame = cap.read()
x, y, width, height = 580, 30, 120, 150
track = (x, y, width, height)

"""
#Getting image of a person from the first frame and forming its histogram
roi = frame[y:y+height, x:x+width]
roi_hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(roi_hsv, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv.calcHist([roi_hsv], [0], mask, [180], [0, 180])
#Normailizing the histogram
#mormalize function returns the histogram normalized to the range [0, 255]
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

#Setting the termination criteria, either 10 iterations or move by atleast 1 pt
term = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

#cv.imshow("roi", roi)



while True:
    ret, frame = cap.read()
    
    if ret == True:
        #converting to HSV
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        #calcBackProject function calculates the back projection of the histogram
        #of the model image and the observed image
        #The function returns the image which shows the position of the model
        #in the observed image
        #The observed image is converted to HSV
        #It takes five arguments:
        #1. The observed image
        #2. The channels of the histogram
        #3. The histogram
        #4. The ranges of the histogram
        #5. The threshold
        bpr = cv.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
        
        #The function cv.meanShift is used to find the new location of the model
        #in the observed image
        #It takes three arguments:
        #1. Back projection of the histogram
        #2. Image of model
        #3. The termination criteria
        #It returns the new location of the model in the observed image
        ret, track = cv.meanShift(bpr, track, term)
        
        x,y,w,h = track
        #Drwaing the rectangle
        final = cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)
        
        cv.imshow("Video", final)
        
        if cv.waitKey(60) == 27:
            break
        
    else:
        break
    

cap.release()

cv.destroyAllWindows()
"""


roi = frame[y:y+height, x:x+width]
roi_hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(roi_hsv, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv.calcHist([roi_hsv], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

term = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

#cv.imshow("roi", roi)



while True:
    ret, frame = cap.read()
    
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        bpr = cv.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
        
        ret, track = cv.CamShift(bpr, track, term)
        
        points = cv.boxPoints(ret)
        points = np.int64(points)
        final = cv.polylines(frame, [points], True, (255,0,0), 2)
        
        cv.imshow("Video", final)
        
        if cv.waitKey(60) == 27:
            break
        
    else:
        break
    

cap.release()

cv.destroyAllWindows()