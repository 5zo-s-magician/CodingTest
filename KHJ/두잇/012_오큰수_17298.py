import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stack = deque()
NGE = [-1] * N

for i in range(N):
    if not stack:
        stack.append(i)
    else:
        while stack and arr[stack[-1]] < arr[i]:
            x = stack.pop()
            NGE[x] = arr[i]
        stack.append(i)

for x in NGE:
    print(x, end=" ")