#-*- coding:utf-8 -*-
# 1. dfs               2. bfs
# - 인접 리스트           - 인접 리스트
# - 방문 확인 리스트       - 방문 확인 리스트
# - 재귀, stack         - queue
# BFS: visited를 미리 해놓고 해야함.
# DFS: visited 검사를 해야함.

import queue
import sys
from collections import deque
from tokenize import Triple
input = sys.stdin.readline

# input processing
N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# 1. dfs
def DFS(V):
    for i in range(1,N+1):
        arr[i].sort(reverse=True)
    visited = [False] * (N+1)
    stack = [V]
    while stack:
        now = stack.pop()
        if visited[now]:
            continue
        visited[now] = True
        print(now, end=" ")
        for i in arr[now]:
            if not visited[i]:
                stack.append(i)
            

def BFS(V):
    for i in range(1,N+1):
        arr[i].sort()
    visited = [False] * (N+1)
    queue = [V]
    visited[V] = True
    while queue:
        now = queue.pop(0)
        print(now, end=" ")
        for i in arr[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
            

DFS(V)
print()
BFS(V)