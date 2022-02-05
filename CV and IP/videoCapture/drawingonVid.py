import cv2 as cv
import datetime as dt

cap = cv.VideoCapture("D:\\videoCapture\\videos\\vid.mkv")

while(cap.isOpened):
    ret, frame = cap.read()
    frame = cv.resize(frame, (800,600))
    
    if ret == True:
        font = cv.FONT_ITALIC
        #datetime.now function returns the current date and time or current timestamp
        text = "Timestamp: - "+str(dt.datetime.now())
        frame = cv.putText(frame, text, (10,100), font, 1, (20,200,200), 4, cv.LINE_AA)
        frame = cv.circle(frame, (400,300), 100, (200,10,200), 5)
        cv.imshow("video", frame)
        
        if cv.waitKey(25)==ord('q'):
            break
        
cap.release()
cv.destroyAllWindows()