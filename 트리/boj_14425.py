
import sys

n,m = map(int,sys.stdin.readline().split())

str_set =[]
check = []
for _ in range(n):
    str_set.append(sys.stdin.readline().rstrip())

for _ in range(m):
    check.append(sys.stdin.readline().rstrip())

ct=0
for val in check:
    if val in str_set:
        ct+=1
print(ct)

