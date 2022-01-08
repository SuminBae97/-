import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
indeg = [0]*(n+1)
q = deque()
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indeg[b]+=1


for i in range(1,n+1):
    if indeg[i]==0:
        q.append(i)

while q:
    val = q.popleft()
    print(val,end=" ")

    for v in graph[val]:
        indeg[v]-=1
        if indeg[v]==0:
            q.append(v)

