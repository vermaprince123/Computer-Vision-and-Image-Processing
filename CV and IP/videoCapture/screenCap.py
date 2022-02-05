import cv2 as c
import pyautogui as p
import numpy as np

res = p.size()


fourcc = c.VideoWriter_fourcc(*"XVID")
output = c.VideoWriter("D:\\videoCapture\\videos\\scrcap.mp4", fourcc, 60.0, res)

c.namedWindow("Screen Record", c.WINDOW_NORMAL)
c.resizeWindow("Screen Record", (600,400))

while True:
    #Taking screenshot
    img = p.screenshot()
    #Converting to numpy array
    frame = np.array(img)
    #Converting from BGR to RGB
    frame = c.cvtColor(frame, c.COLOR_BGR2RGB)
    #Writing to video
    output.write(frame)
    c.imshow("Screen Record", frame)
    
    if c.waitKey(1) == ord('q'):
        break
    

output.release()
c.destroyAllWindows()