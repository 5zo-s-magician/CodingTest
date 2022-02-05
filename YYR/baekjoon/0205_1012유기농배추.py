import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()

        for i in range(4): #상하좌우 네 위치로 좌표 변경
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1: #좌표계 안에서 배추가 심어진 좌표 발견
                q.append((nx, ny))
                graph[nx][ny] = 2 #방문한 좌표 체크
    return 1


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += bfs(i, j)
# 배추가 심어진 곳에서 bfs를 수행함.
# 인접한 배추를 다 체크하면 bfs함수가 1을 반환하기 때문에 이것을 카운트에 추가해줌

    print(cnt)