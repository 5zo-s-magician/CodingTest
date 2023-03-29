import sys
from tokenize import Triple
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(N+1)
count = 0

def dfs(n):
    visited[n] = True
    for x in graph[n]:
        if not visited[x]:
            dfs(x)


for x in range(1,N+1):
    if not visited[x]:
        dfs(x)
        count += 1

print(count)    
    