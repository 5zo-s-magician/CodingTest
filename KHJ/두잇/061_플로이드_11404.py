import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# graph init
graph = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    graph[i][i] = 0
    
for _ in range(M):
    s, e, w = map(int,input().split())
    if graph[s][e] > w:
        graph[s][e] = w

# floyde
for K in range(1,N+1):
    for S in range(1, N+1):
        for E in range(1, N+1):
            if graph[S][E] > graph[S][K] + graph[K][E]:
                graph[S][E] = graph[S][K] + graph[K][E]

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == sys.maxsize:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()