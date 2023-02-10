#-*- coding:utf-8 -*-
import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int,input().split()))
window = deque()

for i in range(N):
    # 만약 window의 끝 값이 현재 값보다 크면 삭제
    while window and window[-1][1] > arr[i]:
        window.pop()
    window.append([i, arr[i]])
    if window[0][0] <= i-L:
        window.popleft()
    print(window[0][1], end=" ")