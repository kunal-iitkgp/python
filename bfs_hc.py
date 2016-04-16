from collections import deque
import numpy
import time
start_x, start_y = [ int(i) for i in raw_input().strip().split() ]
end_x, end_y = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

grid = []
record={}

queue = deque([(start_x,start_y)])
queue1 = deque([(end_x,end_y)])
count =0

grid_1=[]
for i in xrange(0,r):
	grid_1.append(raw_input())

start_time = time.time()
grid = numpy.empty((r,c), dtype = str )
for i in range(0,r):
	for j in range(0,c):
		grid[i][j] = grid_1[i][j]
lists=numpy.zeros((r,c))
parent = numpy.empty((r,c), dtype = tuple )
lists[start_x][start_y]=1


while len(queue)!=0:

	x,y=queue.popleft()
	#print count
	#print x,y
	if end_x==x and end_y==y:
		#print "cool"
		break
	

	else :
		if  y<c-1 :
			#print grid[x][y+1]=='-' , lists[x][y+1]==0
			if (grid[x][y+1]!='%' ) and lists[x][y+1]==0:
				queue.append((x,y+1))
				lists[x][y+1]=1
				parent[x][y+1]=(x,y)
				
				#print " path_x[x][y+1],path_y[x][y+1]",path_x[x][y+1],path_y[x][y+1]
		if x>0:
			#print (grid[x-1][y]=='-' ) , lists[x-1][y]==0
			if (grid[x-1][y]!='%' ) and  lists[x-1][y]==0:
				queue.append((x-1,y))
				lists[x-1][y]=1
				parent[x-1][y]=(x,y)
				
				#print "path_x[x][y-1],path_y[x][y-1] ",path_x[x][y-1],path_y[x][y-1]
		if x<r-1:
			#print grid[x+1][y]=='-' , lists[x+1][y]==0
			if (grid[x+1][y]!='%' ) and lists[x+1][y]==0:
				queue.append((x+1,y))
				lists[x+1][y]=1
				parent[x+1][y]=(x,y)
				
				#print "path_x[x+1][y],path_y[x+1][y] ",path_x[x+1][y],path_y[x+1][y]

		if y>0:
			#print grid[x][y-1]=='-' , lists[x][y-1]==0
			if (grid[x][y-1]!='%') and lists[x][y-1]==0:
				queue.append((x,y-1))
				lists[x][y-1]=1
				parent[x][y-1]=(x,y)
				
				#print "path_x[x][y-1],path_y[x][y-1] ",path_x[x][y-1],path_y[x][y-1]


	#print queue
	#print lists
#print path_x
#print path_y

t_x,t_y=end_x,end_y
while 1:
	#print queue1
	#print path_x[t_x][t_y],path_y[t_x][t_y]
	if t_x==start_x and t_y==start_y:
		#queue1.append((start_x,start_y))
		break
	queue1.append((parent[t_x][t_y]))
	t_x,t_y=parent[t_x][t_y]
	
	#print 	queue1
#print queue1
#print path_x[0.0][2.0], path_y[0.0][2.0]


for i in range(0,len(queue1)):
	p,q=queue1.pop()
	print int(p),int(q)

print len(queue1)

print time.time()-start_time	