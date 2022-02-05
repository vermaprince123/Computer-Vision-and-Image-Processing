import cv2 as cv

#Canny Edge Detection is a popular technique for detecting edges in images, which uses multi-stage algorithm.

#Here, we will make use of Trackbars to adjust the threshold value for Canny Edge Detection.

#Defining a Function
def do_nothing(x):
    pass

#Reading Image
img = cv.imread("D:\\ImgData\\input\\svnit.jpg", 0)
img = cv.resize(img, (600, 385))

#Creating a named Window
cv.namedWindow("Image")
#Creating Trackbar to set threshold value
cv.createTrackbar("Thresh", "Image", 0, 255, do_nothing)

#Setting a Loop to update changes upon Trackbar movement
while True:
    #Reading the Trackbar value
    th =cv.getTrackbarPos("Thresh", "Image")
    #Applying Canny Edge Detection
    canny = cv.Canny(img, th, 255)
    #This function takes three arguments, first is the image, second is the threshold value for the lower end and third is the threshold value for the upper end.
    cv.imshow("Image", canny)
    
    #Waiting for a key to be pressed. (Here 27 is the ASCII value of Esc key)
    if cv.waitKey(1) == 27:
        break

cv.destroyAllWindows()
