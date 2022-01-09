import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph =[[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

answer =[]
def dfs(x):
    global answer
    visited[x]=True
    answer.append(x)

    for node in graph[x]:
        if not visited[node]:
            dfs(node)
dfs(1)
print(len(answer)-1)



