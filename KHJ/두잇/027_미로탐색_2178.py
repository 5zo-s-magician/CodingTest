import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    tmp = input().rstrip()
    graph[i] = [0]+[int(x) for x in tmp]

visited = [[False for _ in range(M+1)] for _ in range(N+1)]
direction = [[-1,0], [0,1], [1,0], [0,-1]]

queue = deque()
queue.append([1,1])
while queue:
    x,y = queue.popleft()
    if [x,y] == [N,M]:
        print(graph[N][M])
        break
    if not visited[x][y]:
        visited[x][y] = True
        for di in direction:
            nx = x + di[0]
            ny = y + di[1]
            if 0 < nx <= N and 0 < ny <= M:
                if graph[nx][ny] != 0:
                    queue.append([nx,ny])
                    graph[nx][ny] = graph[x][y] + 1





# DFS version

# import sys
# from collections import deque
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]

# for i in range(1, N+1):
#     tmp = input().rstrip()
#     graph[i] = [0]+[int(x) for x in tmp]

# visited = [[False for _ in range(M+1)] for _ in range(N+1)]
# direction = [[-1,0], [0,1], [1,0], [0,-1]]
# answer = 1000

# DFS
# def DFS(a, b, c):
#     global answer, N, M
#     if a == N and b == M:
#         if answer > c:
#             answer = c
#             return
#     for di in direction:
#         nx = a+di[0]
#         ny = b + di[1]
#         if 0 < nx <= N and 0 < ny <= M:
#             if graph[nx][ny] == 1 and not visited[nx][ny] and c+1 < answer:
#                 visited[nx][ny] = True
#                 DFS(nx, ny, c+1)
#                 visited[nx][ny] = False

# DFS(1,1,1)
# print(answer)