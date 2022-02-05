import cv2

#Importing an image
#img1 = cv2.imread("D:\\ImgData\\input\\edilogo.jpg", -1)

#Risizing an image
#img1 = cv2.resize(img1, (200,500))

#Flipping an image. Here 0 flips it horizontally, 1 flips it vertically, and -1 flips it both ways.
#img1 = cv2.flip(img1, 0)

#This will print an array of the image
#print(img1)

#This will show the image in a new window named 'The image is... '
#cv2.imshow("The image is...", img1)

#Reading path from user
path = input("Enter the path of image:- ")
#Importing the image from the path
img2 = cv2.imread(path, 0)
#Showing the image
cv2.imshow("Result Image",img2)

k = cv2.waitKey()

if k==ord('s'):
    #Saving the image to a new path
    cv2.imwrite("D:\\ImgData\\output\\img.png",img2)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()

