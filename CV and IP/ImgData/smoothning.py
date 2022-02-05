import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


#Image Smoothing is a technique to reduce noise in an image. Here, we have discused varioud ways to smooth an image, namely filter2D, blur, GaussianBlur, medianBlur, and bilateralFilter.

img = cv.imread("D:\\ImgData\\input\\image.jpg")

#Creating a kernel using numpy. The datatype of elements will be float.
kernel = np.ones((5,5), np.float32)/25
#filer2d method takes three arguments:
#1. src: source image
#2. kernel: kernel to be used for filtering
#3. anchor: anchor point of the kernel  
h_filter = cv.filter2D(img, -1, kernel)

#blur method takes two arguments:
#1. src: source image
#2. ksize: kernel size (kernal size must be odd and greater than 1)
b_filter = cv.blur(img, (7,7))

#GaussianBlur method takes three arguments:
#1. src: source image
#2. ksize: kernel size (kernal size must be odd and greater than 1)
#3. sigmaX: standard deviation in X direction
g_filter = cv.GaussianBlur(img, (5,5), 0)

#medianBlur method takes two arguments:
#1. src: source image
#2. ksize: kernel size (kernal size must be odd and greater than 1)
m_filter = cv.medianBlur(img, 5)

#bilateralFilter method takes four arguments:
#1. src: source image
#2. d: diameter of each pixel neighborhood that is used during filtering
#3. sigmaColor: controls the range of colors that are considered similar
#4. sigmaSpace: controls the range of pixel values that are considered similar
bi_filter = cv.bilateralFilter(img, 9, 75, 75)


#Plotting the images using matplotlib
titles = ['orginal', 'homo', 'blur', 'gblur', 'mblur', 'bilateral']
images = [img, h_filter, b_filter, g_filter, m_filter, bi_filter]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()

#cv.imshow("Image", bi_filter)
#cv.waitKey()
#cv.destroyAllWindows()