import cv2 as cv

img = cv.imread("D:\\ImgData\\input\\numbers.jpg")
img = cv.resize(img, (400,225))

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
__, th1 = cv.threshold(img_gray, 230, 255, cv.THRESH_BINARY_INV)


cnt, heir = cv.findContours(th1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


areas = []
for c in cnt:
    """
    #Array containing image information. 
    moment = cv.moments(c)
    #print("Moment = ", moment)
    #Used to compute center of the countour
    x = int(moment["m10"]/ moment["m00"])
    y = int(moment["m01"]/ moment["m00"])
    
    cv.circle(img1, (x,y), 5, (0,0,0), -1)
    """

    #Below function is used to calculate area of contour
    area = cv.contourArea(c)
    print(area)
    #Adding area to list
    areas.append(area)
    img1 = cv.drawContours(img, [c], -1, (100,200,200), 2)
    
    if area>1000:

        #approx - It is used to approximate shape with least number of edges
        eps = 0.0001*cv.arcLength(c, True)
        data = cv.approxPolyDP(c, eps, True)
        
        #convexHull is used to provide convexity to the contour
        hull = cv.convexHull(data)

        #This function is used to find a rectangle that bounds the Hull. It returns list of x cordinate, y cordinate, width, abd height
        x,y,h,k = cv.boundingRect(hull)
        
        
        img1 = cv.drawContours(img, [hull], -1, (0,0,0), 2)
        img1 = cv.rectangle(img1, (x,y), (x+h, y+k), (200,200,50), 2)
    
    

print(areas)
cv.imshow("Img", img1)
cv.waitKey()
cv.destroyAllWindows()