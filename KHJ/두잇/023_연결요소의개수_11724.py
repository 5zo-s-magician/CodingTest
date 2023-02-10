#-*- coding:utf-8 -*-
# dfs
# 1. 연결리스트로 그래프 표현
# 2. 방문 여부 확인하기
# 3. 스택/재귀

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
answer  = 0

# # 1. stack 기반
# stack = deque()
# for i in range(1,N+1):
#     if visited[i] == False:
#         answer += 1
#         stack.append(i)
#         while stack:
#             now = stack.pop()
#             if visited[now]:
#                 continue
#             visited[now] = True
#             stack += graph[now]

# 2. 재귀 기반
def DFS(now):
    visited[now] = True
    for i in graph[now]:
        if not visited[i]:
            DFS(now)

for i in range(1, N+1):
    if not visited[i]:
        answer += 1
        DFS(i)

print(answer)

    





    