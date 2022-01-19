import sys
sys.setrecursionlimit(10**5)
test_case = int(sys.stdin.readline())

for _ in range(test_case):
	n = int(sys.stdin.readline())


	
	parent = [0]*(n+1)
	level = [0]*(n+1)
	visited = [False]*(n+1)
	tree=[[] for _ in range(n+1)]
	
	for _ in range(n-1):
		a,b = map(int,sys.stdin.readline().split())
		parent[b]=a
		tree[a].append(b)
		tree[b].append(a)
		
		
	def dfs(x,dst):
		visited[x]=True
		level[x] = dst
		
		for node in tree[x]:
			if not visited[node]:
				dfs(node,dst+1)
	
	
	root_index = (parent[1:].index(0)+1)
	dfs(root_index,1)
	
	
	def lcs(a,b):
		while level[a]!=level[b]:
			if level[a] > level[b]:
				a = parent[a]
			else:
				b = parent[b]
			
		while a!=b:
			a = parent[a]
			b = parent[b]
		
		return a
						 
	start,end = map(int,sys.stdin.readline().split())
	print(lcs(start,end))
	
	
	



