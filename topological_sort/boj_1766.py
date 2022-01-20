import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
indeg = [0]*(n+1)
q = deque()

q = []

for i in range(m):
	start,end = map(int,sys.stdin.readline().split())
	indeg[end]+=1
	graph[start].append(end)

	
for i in range(1,n+1):
	if indeg[i]==0:
		q.append(i)

while q:
	val= q.pop(0)
	print(val,end=' ')
	
	
	for node in graph[val]:
		indeg[node]-=1
		
		if indeg[node]==0:
			q.append(node)
					
	q.sort()
