import numpy as np
import cv2
import heapq
from pytesseract import *
from PIL import Image

img = cv2.imread('pics02.jpg',1)

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
height, width = imgray.shape
area_img = height*width
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
	x,y,w,h = cv2.boundingRect(cnt)
	area = w*h
	if area < 0.4*area_img:
		continue

	rect = cv2.minAreaRect(cnt)
	box = cv2.cv.BoxPoints(rect)
	box = np.int0(box)
	cv2.drawContours(img,[box],0,(0,0,255),2)

pts1 = np.float32([box[1], box[2], box[0], box[3]])
w = box[3][0]-box[0][0]
h = box[0][1]-box[1][1]
X = w
Y = h
ordr = [[0,0],[X,0],[0,Y],[X,Y]]
pts2 = np.float32(ordr)

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(X,Y))
rect = dst
rectg = cv2.cvtColor(rect,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(rectg,127,255,0)
kernel = np.ones((17,17),np.uint8)
erosion = cv2.erode(rectg,kernel,iterations = 4)                      
rect = erosion
for i in xrange(len(rect)):
	for j in xrange(len(rect[i])):
		if rect[i][j] < 115:
			rect[i][j] = 0
		else:
			rect[i][j] = 255

cv2.namedWindow("erode", cv2.WINDOW_NORMAL)
cv2.imshow("erode", erosion)

edges = cv2.Canny(rect,70,100)
contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

visited = np.zeros((X,Y))
data = np.empty((X,Y), dtype = tuple )
heap = []

area_img = X*Y
for cnt in contours:
	x,y,w,h = cv2.boundingRect(cnt)
	area = w*h
	if area > 0.8*area_img or area <0.001*area_img:
		continue
	heapq.heappush(heap, ( y , (x,y,w,h) ))
	

for i in xrange(len(heap)):
	(y , (x,y,w,h)) = heapq.heappop(heap) 
	if visited[x][y]==0:
		for i in range(0,10):
			visited[x][y+i]=1
			visited[x][y-i]=1
			visited[x+i][y]=1
			visited[x-i][y]=1
		visited[x][y]=1
		rect = dst[y:y+h, x:x+w]
		cv2.rectangle(dst,(x,y),(x+w,y+h),(125,255,125),2)
		rectg = cv2.cvtColor(rect,cv2.COLOR_BGR2GRAY)
		for i in xrange(len(rectg)):
			for j in xrange(len(rectg[i])):
				if rectg[i][j] < 120:
					rectg[i][j] = 0
				else:
					rectg[i][j] = 255

		height, width = rectg.shape
		rectg = cv2.resize(rectg, (width*2, height*2), interpolation=cv2.INTER_AREA)
		cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
		cv2.imshow("Image", rectg)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		pil_im = Image.fromarray(rect)
		print image_to_string(pil_im)

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()