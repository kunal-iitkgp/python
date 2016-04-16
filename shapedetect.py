from numpy import *
import cv2
from matplotlib import pyplot as plt
cv2.namedWindow("canny Image")
cv2.namedWindow(" Image")


img = cv2.imread('18.jpg',1)
#gray = cv2.imread('15.jpg',0)
edges = cv2.Canny(img,100,500)
#im1 = edges
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
cv2.imshow("canny Image", edges)
#ret,thresh = cv2.threshold(gray,127,255,0)
contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img, contours, -1, (125,125,125), 5)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.055*cv2.arcLength(cnt,True),True)
    print len(approx)
    if len(approx)==3:
        print "triangle"
        cv2.drawContours(img,[cnt],0,(255,255,255),3)
    elif len(approx)==4:
        print "square"
        cv2.drawContours(img,[cnt],0,(0,0,255),3)
    


cv2.imshow(" Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
