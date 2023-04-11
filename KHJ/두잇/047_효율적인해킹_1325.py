import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
answer = [0] * (N+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                queue.append(i)
                

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(1,N+1):
    visited = [False]*(N+1)
    BFS(i)

maxVal = 0
for i in range(1, N+1):
    maxVal = max(maxVal, answer[i])

for i in range(1, N+1):
    if answer[i] == maxVal:
        print(i, end=' ')        