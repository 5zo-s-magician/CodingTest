
# dfs: 깊이 우선 탐색
# 밑으로 쭉 드감.
# 스택 혹은 재귀함수 사용!
# 1 넣어 -> 자식 다 조지고 위로 넘어가는 느낌?
def dfs(graph, v, start, already):
    #print(start, end = " ")

           
           
    for i in range(1, v+1):
       if graph[start][i] == 1 and i not in already:
            graph[start][i] = 0
            graph[i][start] = 0
            already.append(i)
            dfs(graph, v, i, already)
    return already

# 너비 우선 탐색
def bfs(graph1, v, start, already):
    #print(start, end=" ")
    node = [start] 
    while node:
        now = node.pop(0)
        for i in range(1, v+1):
            if graph2[now][i] == 1 and i not in already:
                #print(i, end=" ")
                graph2[now][i] = 0
                graph2[i][now] = 0
                node.append(i)
                already.append(i)
    answer = ""
    for i in range(len(already)):
        if i == v-1:
            answer += str(already[i])
        else:
            answer += str(already[i])+" "
    print(answer)
    return


v, e, start = map(int,input().split())
# 정점 개수 만큼 있음!
graph1 = [[0 for i in range(v+1)] for j in range(v+1)]
graph2 = [[0 for i in range(v+1)] for j in range(v+1)]
# 인접한 놈들 = 1 -> 인접 행렬 만들기
for i in range(e):
    a, b = map(int,input().split())
    graph1[a][b] = 1
    graph1[b][a] = 1
    graph2[a][b] = 1
    graph2[b][a] = 1
already = dfs(graph1, v, start, [start])

answer = ""
for i in range(len(already)):
    if i == v-1:
        answer += str(already[i])
    else:
        answer += str(already[i])+" "
print(answer)

bfs(graph2, v, start, [start])
