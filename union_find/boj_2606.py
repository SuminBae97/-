import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i]=i


def get_parent(x):
    if parent[x]==x:
        return x
    else:
        y = get_parent(parent[x])
        parent[x] = y
        return y

def union(x,y):
    px = get_parent(x)
    py = get_parent(y)

    if px!=py:
        parent[py]=px

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    union(a,b)

ct=0
for i in range(2,len(parent)):
    if get_parent(1)==get_parent(i):
        ct+=1
print(ct)

