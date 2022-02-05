#AND, OR, NOT, XOR
"""
AND --> both the args are True
OR --> either of the args is True
NOT --> when the arg is false
XOR --> both args are different
"""

import cv2 as cv
import numpy as np

img1 = np.zeros((360,640,3), np.uint8)
img1 = cv.rectangle(img1, (50,50), (200,250), (255,255,255), -1)

img2 = np.zeros((360,640,3), np.uint8)
img2 = cv.rectangle(img2, (100,180), (150,300), (255,255,255), -1)

#bitand = cv.bitwise_and(img1,img2)
#bitor = cv.bitwise_or(img1,img2)
#bitnot = cv.bitwise_not(img2)
bitxor = cv.bitwise_xor(img1,img2)

#cv.imshow("Img1", img1)
#cv.imshow("Img2", img2)
cv.imshow("Image", bitxor)

cv.waitKey()
cv.destroyAllWindows()