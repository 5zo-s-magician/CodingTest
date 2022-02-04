# 이문제는  dfs를 하면 되지 않을까? -> 가면서 1이 있으면 끝까지 파고들어서 개수세기 -> 개수를 이미 센거는 2같은거로 표시

def solution(ga, se, num, graph):
    count = 0
    for i in range(ga):
        for j in range(se):
            if graph[j][i] == 1:
                dfs(ga, se, j,i, graph)
                count += 1
    print(count)
    return
    
    
# def dfs(ga, se, a,b, graph):
#     dx = [0, +1, 0, -1]
#     dy = [+1, 0, -1, 0]
#     graph[a][b] = 2
#     for i in range(4):
#         nx = dx[i] + a
#         ny = dy[i] + b
#         if -1<nx<se and -1<ny<ga and graph[nx][ny] == 1:
#             dfs(ga, se, nx, ny, graph)
#     return graph
            
def dfs(ga, se, a, b, graph):
    dx = [0, +1, 0, -1]
    dy = [+1, 0, -1, 0]
    stack = [[a,b]]
    while stack:
        now = stack.pop()
        graph[now[0]][now[1]] = 2
        for i in range(4):
            nx = dx[i] + now[0]
            ny = dy[i] + now[1]
            if -1<nx<se and -1<ny<ga and graph[nx][ny] == 1:
                stack.append([nx, ny])
        
    
    
num = int(input())
for i in range(num):
    ga, se, num2 = map(int,input().split())
    graph= [[0]* ga for k in range(se)]
    for j in range(num2):
        a, b = map(int,input().split())
        graph[b][a] = 1
        
    solution(ga,se,num2,graph)