#DFS,BFS를 모두 편하게 구현하게 위해 양방향 큐 import
from collections import deque 

#DFS 구현
def dfs(node):
    if check[node] == 0:#정점을 방문하지 않았을 시 탐색(print)
        print(node, end=' ') 
        check[node] = 1 #방문 노드 표시
        for n in sorted(li[node]): #숫자가 작은 번호의 정점부터 탐색
            dfs(n)

#BFS 구현
def bfs(start):
    queue = deque([start])
    while queue:
        node = queue.popleft()#제일 왼쪽 정점 pop
        print(node, end=' ')
        check[node] = 1 #방문 노드임을 표시
        for n in sorted(li[node]):  #숫자가 작은 번호의 정점부터 탐색
            if check[n] == 0:#정점을 방문하지 않았을 시 탐색(print)
                queue.append(n) #갈수있는 노드들을 append 후 방문 처리하기
                check[n] = 1 

#주어진 정점, 간선, 연결 정보 각 변수에 저장하기
N, M, V = map(int, input().split())

li = [[] for _ in range(N+1)]

#양방향 연결
for _ in range(M):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)
#dfs 탐색 시작
check = [0]*(N+1)#방문 기록 초기화
dfs(V)
print()
#bfs 탐색시작
check = [0]*(N+1)#방문 기록 초기화
bfs(V)