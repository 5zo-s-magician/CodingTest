from collections import deque

def dijkstra(cave, N):
    #상하좌우
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    theif = [[99999 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((0,0))
    theif[0][0] = cave[0][0]
    
    while q:
        i, j = q.popleft()
        
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if theif[nx][ny] > theif[i][j] + cave[nx][ny]:
                    theif[nx][ny] = theif[i][j] + cave[nx][ny]
                    q.append((nx,ny))
    return theif[N-1][N-1]
    

cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = dijkstra(graph, N)
    print("Problem {0}: {1}".format(cnt, answer))
    
    cnt += 1