import sys
sys.setrecursionlimit(10**5)

test_case = int(sys.stdin.readline())

for _ in range(test_case):
	n,m = map(int,sys.stdin.readline().split())
	graph=[[] for _ in range(n+1)]
	visited = [False]*(n+1)
	
	for _ in range(m):
		a,b = map(int,sys.stdin.readline().split())
		graph[a].append(b)
		graph[b].append(a)
	
	count=0	
	def dfs(x):
		global count
		count+=1
		visited[x]=True
		
		for node in graph[x]:
			if not visited[node]:
				dfs(node)
				
				
	dfs(1)
	print(count-1)	
		


