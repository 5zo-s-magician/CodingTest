from collections import deque

n, m, v = map(int, input().split())

graph_array = []

already_b = []
already_d = []

for i in range(0, m+1):
    already_b.append(0)
    already_d.append(0)

def dfs(v):
    already_d[v] = 1
    print(v, end = " ")
    for i in range(1, n+1):
        if already_d[i] == 0 and graph_array[v][i] == 1:
            dfs(i)

def bfs(v):
    tmp_deque = deque()
    tmp_deque.append(v)
    already_b[v] = 1
    while tmp_deque:
        v = tmp_deque.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if already_b[i] == 0 and graph_array[v][i] == 1:
                tmp_deque.append(i)
                already_b[i] = 1

for i in range(0, m+1):
    graph_array.append([])
    for j in range(0, m+1):
        graph_array[i].append(0)

for i in range(0, m+1):
    a, b = map(int, input().split())
    graph_array[a][b] = 1

dfs(v)
print()
bfs(v)