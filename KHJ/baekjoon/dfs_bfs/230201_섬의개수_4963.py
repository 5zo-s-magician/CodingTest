import sys
sys.setrecursionlimit(10**6)

def island_count(graph, w, h):
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] != 1:
                continue
            cnt += 1
            graph = dfs(graph, i, j, w, h)
    return cnt
            

def dfs(graph, x, y, w, h):
    graph[x][y] = 2
    for i in [-1,0,1]:
      for j in [-1,0,1]:
        if 0<=x+i<h and 0<=y+j<w and graph[x+i][y+j] == 1:
          graph = dfs(graph, x+i, y+j, w, h)
    return graph

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    print(island_count(graph, w, h))