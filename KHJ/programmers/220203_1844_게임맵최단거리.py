# 최단거리 -> bfs 사용하면 될 것 같은 기분?
# 효율성 레전드였다~

def solution(maps):
    start = [0,0]
    node = [start]
    n = len(maps)
    m = len(maps[0])
    cost = [[1] * m for i in range(n)]
    #visited = []
    dx = [-1, 0, +1, 0]
    dy = [0, +1, 0 ,-1]
    while node:
        now = node.pop(0) 
        if now == [n-1, m-1]:
            return cost[now[0]][now[1]]
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] == 1:
                    #if [nx,ny] not in visited:
                    cost[nx][ny] = cost[now[0]][now[1]] +1
                    maps[nx, ny] = 1
                    node.append([nx,ny])
                        #visited.append(now)

    
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))