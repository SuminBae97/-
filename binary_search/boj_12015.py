import sys
n= int(sys.stdin.readline())

seq = list(map(int,sys.stdin.readline().split(" ")))

#answer[i] 의미:
#길이가 i 인 부분수열 중에서 가장 뒤에 올 수 있는 값이다
# this is lower bound
answer=[0]

for val in seq:
	if answer[-1]< val:
		answer.append(val)

	else:
		left = 0
		right = len(answer)
		
		while left<right:
			mid = (left+right)//2
			
			if answer[mid] < val:
				left = mid+1
			else:
				right = mid
		answer[right] = val		
			
print(len(answer)-1)
print(answer)
