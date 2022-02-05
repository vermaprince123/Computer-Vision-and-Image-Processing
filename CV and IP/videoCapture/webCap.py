import cv2 as c

camera = "http://192.168.128.42:8080/video"
cap = c.VideoCapture(0, c.CAP_DSHOW)
cap.open(camera)
print(cap.isOpened())

#fourcc is the codec used to encode the video
fourcc = c.VideoWriter_fourcc(*'XVID')

#This function takes the video and the codec and saves it
#It takes four parameters:
#1. The path and name of the file
#2. The codec
#3. The frame rate
#4. The resolution
output = c.VideoWriter("D:\\videoCapture\\videos\\outvideo.mp4", fourcc, 20.0, (640, 480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        gray = c.cvtColor(frame, c.COLOR_BGR2GRAY)
        c.imshow('Web Cam Capture',frame)
        output.write(frame)
        if c.waitKey(25) == ord('q'):
            break
        

cap.release()
output.release()
c.destroyAllWindows()