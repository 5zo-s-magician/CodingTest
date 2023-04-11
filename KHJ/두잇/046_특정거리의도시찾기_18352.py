import sys
from collections import deque
input = sys.stdin.readline


N, M, K, X = map(int, input().split())
A = [[] for _ in range(N+1)]
queue = deque()
visited = [False for _ in range(N+1)]
dist = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    A[a].append(b)

queue.append(X)
answer = []

while queue:
    now = queue.popleft()
    #print(now)
    if not visited[now]:
        visited[now] = True
        for x in A[now]:
            if not visited[x] and dist[x] == 0:
                dist[x] = dist[now] + 1
                if dist[x] == K:
                    answer.append(x)
                queue.append(x)
                #print(queue, dist, visited)
        
if answer:
    answer.sort()
    for x in answer:
        print(x)
else:
    print(-1)