from re import L
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, S = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited_DFS = [False]*(N+1)
visited_BFS = [False]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort()

def DFS(N):
    print(N, end=" ")
    visited_DFS[N] = True
    for x in graph[N]:
        if not visited_DFS[x]:
            DFS(x)
        
def BFS(N):
    queue = deque()
    queue.append(N)
    while queue:
        now = queue.popleft()
        if not visited_BFS[now]:
            print(now, end=" ")
            visited_BFS[now] = True
            for x in graph[now]:
                queue.append(x)
            
DFS(S)
print()
BFS(S)   
    