from collections import deque
import heapq
import numpy
from math import sqrt
import time
import numpy as np
import cv2

start_x, start_y = [ int(i) for i in raw_input().strip().split() ]
end_x, end_y = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

img = cv2.imread("1.png",0)
img = cv2.resize(img, (r,c), interpolation=cv2.INTER_AREA)
ret,img = cv2.threshold(img,127,255,0)
#cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
#cv2.imshow("Image", img)

save = img
visited = numpy.zeros((r,c))
h_cost = numpy.zeros((r,c))
f_cost = numpy.zeros((r,c))
g_cost = numpy.zeros((r,c))
parent = numpy.empty((r,c), dtype = tuple )

def MoveCost((x_1,y_1),(x_2,y_2)):
	return (x_2-x_1)**2 + (y_2 - y_1)**2

def heuristicCost(x,y):
	global end_x,end_y
	return ((abs(end_x - x) + abs(end_y - y)) )
e = 1.6
k = 1


h_cost[start_x][start_y] = heuristicCost(start_x,start_y)
g_cost[start_x][start_y] = 0
f_cost[start_x][start_y] = e * h_cost[start_x][start_y]
parent[start_x][start_y] = (start_x,start_y)
openn = []
incons = []
heapq.heappush( openn, ( f_cost[start_x][start_y] , (start_x,start_y) ) )
visited[start_x][start_y] = 1

while e>0.7:
	while 1:
		#print openn
		(fcost,(cord_x,cord_y)) = heapq.heappop(openn)
		img[cord_x][cord_y] = 125
		if (cord_x == end_x and cord_y == end_y ):
			break

		else :
			for i in range(-1,2):
				    for j in range(-1,2):
				    	if i == -1 :
				    		if cord_x<1:
				    			continue
				    	if i == 1:
				    		if cord_x == r-1:
				    			continue
				    	if j == -1:
				    		if cord_y<1:
				    			continue
				    	if j == 1:
				    		if cord_y == c-1:
				    			continue
				    	if i==0 and j==0:
				    		continue
				    	if (img[cord_x+i][cord_y+j]!= 0 ) :
				    		if visited[cord_x+i][cord_y+j]==0:
				    			visited[cord_x+i][cord_y+j] = 1
				    			h_cost[cord_x+i][cord_y+j] = heuristicCost(cord_x+i,cord_y+j)
				    			g_cost[cord_x+i][cord_y+j] = g_cost[cord_x][cord_y] + MoveCost((cord_x+i,cord_y+j),(cord_x,cord_y))
				    			f_cost[cord_x+i][cord_y+j] = e * h_cost[cord_x+i][cord_y+j] + g_cost[cord_x+i][cord_y+j]
				    			parent[cord_x+i][cord_y+j] = (cord_x,cord_y)
				    			heapq.heappush( openn, ( f_cost[cord_x+i][cord_y+j], (cord_x+i,cord_y+j)))

				    		else :
				    			up_gcost = g_cost[cord_x][cord_y] + MoveCost((cord_x+i,cord_y+j),(cord_x,cord_y))
				    			if up_gcost < g_cost[cord_x+i][cord_y+j]  :
				    				#parent[cord_x+i][cord_y+j] = (cord_x,cord_y)
				    				g_cost[cord_x+i][cord_y+j] = up_gcost
				    				f_cost[cord_x+i][cord_y+j] = e * h_cost[cord_x+i][cord_y+j] + g_cost[cord_x+i][cord_y+j]
				    				heapq.heappush( incons, ( f_cost[cord_x+i][cord_y+j], (cord_x+i,cord_y+j)))
				    			else :
				    				pass
	'''queue1 = deque([(end_x,end_y)])
	t_x,t_y=end_x,end_y
	while 1:
		if t_x==start_x and t_y==start_y:
			break
		queue1.append(parent[t_x][t_y])
		t_x,t_y = parent[t_x][t_y]
		print queue1

	print len(queue1)-1

	for i in range(0,len(queue1)):
		p,q = queue1.pop()
		#print int(p),int(q)
		img[int(p)][int(q)] = 50 
	queue1.clear()'''

	#cv2.namedWindow("Image1" + str(k), cv2.WINDOW_NORMAL)
	#cv2.imshow("Image1" + str(k), img)
	cv2.imwrite("Image1" + str(k) + ".png", img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	print("--------------------------------------------------------------")
	e = e - 0.2
	k = k + 1
	img = save
	new = []
	print len(openn), len(incons)
	for i in range(0,len(incons)):
		heapq.heappush( openn, ( heapq.heappop(incons) ) )
	print len(openn)
	#time.sleep(5)
 	for i in range(0,len(openn)):
		(key,(x,y)) = heapq.heappop(openn)
		key = g_cost[x][y] + e * h_cost[x][y]
		heapq.heappush(new, (key, (x,y))) 
	openn = new

	#openn = []
	#heapq.heappush( openn, ( f_cost[start_x][start_y] , (start_x,start_y) ) )
	incons = []
	visited = numpy.zeros((r,c))
	#parent = numpy.empty((r,c), dtype = tuple )
	f_cost[start_x][start_y] = e * h_cost[start_x][start_y]
	parent[start_x][start_y] = (start_x,start_y)
	#visited[start_x][start_y] = 1
	