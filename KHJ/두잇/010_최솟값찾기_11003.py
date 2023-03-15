#-*- coding:utf-8 -*-
# import sys
# from collections import deque
# input = sys.stdin.readline

# N, L = map(int, input().split())
# arr = list(map(int,input().split()))
# window = deque()

# for i in range(N):
#     # 만약 window의 끝 값이 현재 값보다 크면 삭제
#     while window and window[-1][1] > arr[i]:
#         window.pop()
#     window.append([i, arr[i]])
#     if window[0][0] <= i-L:
#         window.popleft()
#     print(window[0][1], end=" ")


import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))
deq = deque()

for i in range(N):

    start  = i - L + 1 if (i - L + 1) >= 0 else 0

    while deq and deq[-1][1] > arr[i]:
        deq.pop()
    deq.append([i, arr[i]])
    while deq[0][0] < i - L + 1:
        deq.popleft()
    
    print(deq[0][1], end=" ")



import sys
from collections import deque
input = sys.stdin.readline
N, L = map(int, input().split())
arr = list(map(int, input().split()))
deq = deque()
deq.append([0, arr[0]])
print(deq[0][1], end=" ")
for i in range(1, N):
    start  = i - L + 1 if (i - L + 1) >= 0 else 0
    # 2. 맨 앞 범위 확인
    while deq and deq[0][0] < start:
        deq.popleft()
    # 3. 맨 뒤 젤 작은지 확인
    while deq and deq[-1][1] > arr[i]:
        deq.pop()
    deq.append([i, arr[i]])
    
    print(deq[0][1], end=" ")