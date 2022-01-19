import sys
sys.setrecursionlimit(10**5)
n = int(sys.stdin.readline())
visited = [False]*(n+1)
parent = [0]*(n+1)
level = [0]*(n+1)
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
	a,b = map(int,sys.stdin.readline().split())
	tree[a].append(b)
	tree[b].append(a)
	
def dfs(x,dst):
	visited[x]=True
	level[x] = dst
	
	for node in tree[x]:
		if visited[node]==False:
			parent[node]=x
			dfs(node,dst+1)
	
		
def lcs(a,b):
	#until same height
	while level[a]!=level[b]:
		if level[a]>level[b]:
			a = parent[a]
		else:
			b = parent[b]
	
	#after making same height
	#start check least common 			
	while a!=b:
		a=parent[a]
		b=parent[b]
	
	return a
		
		
dfs(1,0)


m = int(sys.stdin.readline())

for _ in range(m):
	a,b = map(int,sys.stdin.readline().split())
	print(lcs(a,b))
		
		



