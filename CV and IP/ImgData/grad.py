import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


#Directional change in color or intensity of an image is known as gradient. Gradient methods are used to detect edges in an image.

#The methods discussed here are Sobel and Laplacian.

img = cv.imread("D:\\ImgData\\input\\childimg.jpeg", 0)
#img = cv.resize(img, (640, 360))

#Laplaciam method takes three arguments:
#1. src: Source image
#2. dtype: Type for negative values
#3. ksize: Aperture size (Must be odd)
lap = cv.Laplacian(img, cv.CV_64F, ksize=5)
#We neew to convert this image to 8-bit unsigned integer type for displaying the result.
lap = np.uint8(np.absolute(lap))

#Sobel method takes five arguments:
#1. src: Source image
#2. dtype: Type for negative values
#3. dx: Derivative order in x
#4. dy: Derivative order in y
#5. ksize: Aperture size (Must be odd)

#Here dx will be 1 and dy will be 0.
sobel_x = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
sobel_x = np.uint8(np.absolute(sobel_x))
#Here dx will be 0 and dy will be 1.
sobel_y = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
sobel_y = np.uint8(np.absolute(sobel_y))
#Combining x and y gradient
sobel = cv.bitwise_or(sobel_x, sobel_y)


#Plotting the images using matplotlib
images = [img, lap, sobel_x, sobel_y, sobel]
titles = ['original', 'lap', 'sobelx', 'sobely', 'sobelc']
for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.xticks([])

plt.show()

"""
cv.imshow("Image", sobel)
cv.waitKey()
cv.destroyAllWindows()
"""