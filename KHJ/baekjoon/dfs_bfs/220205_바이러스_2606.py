def solution(graph, computer_num):
    count = 0
    #for i in range(1, computer_num+1):
    for j in range(1, computer_num+1):
            if graph[1][j] == 1:
                count =  dfs(graph, i, j, computer_num, count)
                
    print(count)
    return
    
    
# def dfs(graph, a, b, num):
#     dx = [0, +1, 0, -1]
#     dy = [+1, 0, -1, 0]
#     graph[a][b] = 2
#     graph[b][a] = 2
#     for i in range(4):
#         nx = a + dx[i]
#         ny = b + dy[i]
#         if 0<nx<num+1 and 0<ny<num+1 and graph[nx][ny] == 1:
#             dfs(graph,a,b,num)
#     return graph
# dfs 그냥 무조건 recursion 말고 stack으로다가 하는게 나을듯... 준내 안되네 진짜
def dfs(graph, a, b, num, count):
    # dx = [0, +1, 0, -1]
    # dy = [+1, 0, -1, 0]
    stack = [[a,b]]
    while stack:
        a, b = stack.pop()
        if graph[a][b] ==2:
            continue
        graph[a][b] = 2
        graph[b][a] = 2
        count += 1
        for i in range(1, num+1):
            ny = b + i
            if 0<ny<num+1 and graph[a][ny] == 1:
                stack.append([a,ny])
        for i in range(1, num+1):
            nx = a + i
            if 0<nx<num+1 and graph[nx][b] == 1:
                stack.append([nx,b])
    return count



computer_num = int(input())
conn_num = int(input())
graph = [[0]*(computer_num+1) for i in range(computer_num+1)]
for i in range(conn_num):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

solution(graph, computer_num)