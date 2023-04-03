import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline

N = int(input())
arr = [0]*N
answer = 0

for i in range(N):
    arr[i] = int(input())

heapify(arr)

while len(arr) >1:
    a = heappop(arr)
    b = heappop(arr)
    tmp = a + b
    answer += tmp
    heappush(arr, tmp)


print(answer)
