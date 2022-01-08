import sys
n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n + 1)]


def Find(x):
  if parent[x]==x:
      return x

  else:
      y = Find(parent[x])
      parent[x]=y
      return y



def Union(x, y):
    xp = Find(x)
    yp = Find(y)

    if xp!=yp:
        parent[yp] = xp

for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())

    if command == 0:  
        Union(a, b)


    elif command == 1:
        a_parents = Find(a)
        b_parents = Find(b)
        if a_parents == b_parents:
            print("YES")
        else:
            print("NO")
