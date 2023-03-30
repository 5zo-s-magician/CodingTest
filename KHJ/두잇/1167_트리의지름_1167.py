import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for i in range(N):
    tmp = list(map(int, input().split()))
    k = tmp[0]
    x = 1
    while tmp[x] != -1:
        graph[k].append((tmp[x], tmp[x+1]))
        x += 2


def BFS(N):
    queue = deque()
    queue.append(N)

    while queue:
        now = queue.popleft()
        if not visited[now]:
            visited[now] = True
            for x,dist in graph[now]:
                if not visited[x]:
                    queue.append(x)
                    node[x] = node[now]+dist

node = [0]*(N+1)
visited = [False]*(N+1)

BFS(1)
max = 0
mnode = 1
for i,x in enumerate(node):
    if max<x:
        mnode = i
        max = x

node = [0]*(N+1)
visited = [False]*(N+1) 
BFS(mnode)
max = 0
mnode = 1
for i,x in enumerate(node):
    if max<x:
        mnode = i
        max = x
print(max)
