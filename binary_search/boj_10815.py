import sys

n= int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split(" ")))
m = int(sys.stdin.readline())
search_card = list(map(int,sys.stdin.readline().split(" ")))

card.sort()


def binary_search(target):
    left = 0
    right = len(card)-1

    while left<=right:
        mid = (left+right)//2
        if card[mid]==target:
            return 1
        elif card[mid] > target:
            right = mid-1
        else:
            left = mid+1

    return 0

answer=[]
for val in search_card:
    answer.append(binary_search(val))
    
for v in answer:
    print(v,end=' ')
