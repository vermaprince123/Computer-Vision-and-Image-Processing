import cv2 as cv


#Reading a Haaarcascade file which is similar to reading an input dataset in Machine Learning. We can also make our own file, but here we are using one which is already made.
cat = cv.CascadeClassifier("D:\\ImgData\\input\\haarcascade_frontalcatface.xml")

#Reading an image and converting it into gray scale. (Most of the functions process gray scale images)
img = cv.imread("D:\\ImgData\\input\\catdog.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Detecting cat face
cats = cat.detectMultiScale(img_gray, 1.1, 1)
#detectMultiScale function takes 3 to 5 arguments, first one being the image, second one being scale_factor to reduce image size, third one being minimum neighbours.
#It returns an array tuples containing x coordinate, y coordinate, width, and height.

#Setting a for loop to show all the detected faces.
for (x,y,w,h) in cats:
    img = cv.rectangle(img, (x,y), (x+w,y+h), (200, 150, 150), 4)

img = cv.resize(img, (512, 366))
cv.imshow("Cat", img)
cv.waitKey()
cv.destroyAllWindows()