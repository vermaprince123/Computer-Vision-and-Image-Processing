import cv2 as cv

#We can remove background from an image using the background subtraction method.
#Here we have discussed two methods, one being KNN(K Nearest Neighbours) and the other being MOG2.

cap = cv.VideoCapture("D:\\videoCapture\\videos\\test.mp4")

#These methods take one parameter, detectShadows, which is a boolean value.
algo_1 = cv.createBackgroundSubtractorMOG2(detectShadows = True)
algo_2 = cv.createBackgroundSubtractorKNN(detectShadows = True)


while True:
    __, frame = cap.read()
    frame = cv.resize(frame, (600,400))
    
    if frame is None:
        break
    #Applying algorithm over images
    alg1 = algo_1.apply(frame)
    alg2 = algo_2.apply(frame)
    
    cv.imshow('video', alg1)
    
    if cv.waitKey(60) == 27:
        break
    

cap.release()
cv.destroyAllWindows()