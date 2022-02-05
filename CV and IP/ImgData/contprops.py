import cv2 as cv
import numpy as np

hand = cv.imread("D:\\ImgData\\input\\hand.jpg")
hand_gray = cv.cvtColor(hand, cv.COLOR_BGR2GRAY)

__, th1 = cv.threshold(hand_gray,225, 255, cv.THRESH_BINARY_INV)

#Sharpning Image for accurate results
kernel = np.ones((6,6), np.uint8)
th1 = cv.erode(th1, kernel)

cnts, heir = cv.findContours(th1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


for c in cnts:
    epsilon = 0.0001*cv.arcLength(c, True)
    data = cv.approxPolyDP(c, epsilon, True)
    hull1 = cv.convexHull(data)
    
    hand_cnt = cv.drawContours(hand, [c], -1, (255,0,0), 2)
    hand_cnt = cv.drawContours(hand, [hull1], -1, (0,0,255), 2)
    

hull2 = cv.convexHull(cnts[0], returnPoints = False)
#convexityDefects returns an array which contain value  [start_point, end_point, farthest_point, approximate_distance to farthest point ]
defect = cv.convexityDefects(cnts[0], hull2)

#Showing convexity defects in image
for i in range(defect.shape[0]):
   s, e, f, d = defect[i, 0]
   start = tuple(c[s][0])
   end = tuple(c[e][0])
   far = tuple(c[f][0])
   cv.line(hand_cnt,start,end,[255,0,0],2)
   cv.circle(hand_cnt, far, 5, (0,255,0), -1)
   

#Finding extreme points - topmost, bottommost, leftmost, rightmost


c_max = max(cnts, key=cv.contourArea)

extL = tuple(c_max[c_max[:,:,0].argmin()][0]) #Extreme Left
extR = tuple(c_max[c_max[:,:,0].argmax()][0]) #Extreme Right
extT = tuple(c_max[c_max[:,:,1].argmin()][0]) #Extreme Top
extB = tuple(c_max[c_max[:,:,1].argmax()][0]) #Extreme Bottom


#Showing extreme points in image
cv.circle(hand_cnt, extL, 5, (255,255,0), -1)
cv.circle(hand_cnt, extR, 5, (0,255,255), -1)
cv.circle(hand_cnt, extT, 5, (255,0,255), -1)
cv.circle(hand_cnt, extB, 5, (255,255,100), -1)

    

cv.imshow("Hand", hand_cnt)
cv.waitKey()
cv.destroyAllWindows()