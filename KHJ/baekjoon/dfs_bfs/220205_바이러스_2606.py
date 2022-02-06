def solution(graph, computer_num):
    node = []
    #for i in range(1, computer_num+1):
    for j in range(1, computer_num+1):
            if graph[1][j] == 1:
                node =  dfs(graph, 1, j, computer_num, node)  
    if 1 in node:
        print(len(node)-1)
        return
    print(len(node))
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
def dfs(graph, a, b, num,node):
    stack = [[a,b]]
    while stack:
        a, b = stack.pop()
        if graph[a][b] ==2:
            continue
        if graph[b][a] ==2:
            continue
        graph[a][b] = 2
        graph[b][a] = 2
        if a not in node:
            node.append(a)
        if b not in node:
            node.append(b)
        for i in range(1, num+1):
            if graph[a][i] == 1:
                stack.append([a,i])
        for i in range(1, num+1):
            if graph[i][b] == 1:
                stack.append([i,b])
    return node



computer_num = int(input())
conn_num = int(input())
graph = [[0]*(computer_num+1) for i in range(computer_num+1)]
for i in range(conn_num):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

solution(graph, computer_num)