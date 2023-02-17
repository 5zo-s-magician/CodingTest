import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edge_graph = [[]]
for _ in range(M):
    s, e, w = map(int, input().split())
    edge_graph.append((s,e,w))
distance = [sys.maxsize]*(N+1)
distance[1] = 0

for i in range(N):
    for j in range(1, M+1):
        s, e, w = edge_graph[j]
        if distance[s] != sys.maxsize and distance[e] > distance[s]+w:
            distance[e] = distance[s]+w

# check if this graph has minus loop
check = [i for i in distance]
for j in range(1, M+1):
        s, e, w = edge_graph[j]
        if check[s] != sys.maxsize and check[e] > check[s]+w:
            check[e] = check[s]+w 

if check != distance:
    print(-1)
else:
    for i in range(2,N+1):
        if distance[i] == sys.maxsize:
            print(-1)
        else:
            print(distance[i])