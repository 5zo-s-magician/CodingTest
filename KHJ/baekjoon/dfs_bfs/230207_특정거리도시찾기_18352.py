from collections import deque

def distance(graph, N, X):
    dist = [-1] * (N+1)
    dist[X] = 0
    deq = deque([X])
    
    while deq:
        now = deq.popleft()
        for x in graph[now]:
            if dist[x] == -1:
                dist[x] = dist[now] + 1
                deq.append(x) 

    return dist
def answer(dist, K):
    if K not in dist:
        print(-1)
    else:
        for idx, x in enumerate(dist):
            if x == K:
                print(idx)

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

dist = distance(graph, N, X)
answer(dist, K)