#바이러스 문제가 dfs인 이유: 트리 전체 탐색 필요하기 때문!
#인풋처리부분

n = int(input())		#컴퓨터 수
m = int(input())		#연결된 컴퓨터 쌍의 수

# 인접리스트 graph 선언 및 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(m):							
# 연결된 컴퓨터 쌍의 수만큼 반복
    x, y = map(int, input().split())		
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)	#전부 방문횟수 0으로 초기화하기

#dfs함수 만들기
def dfs(graph, v, visited):
    visited[v] = 1 #방문했기때문에 1로 표시
    for i in graph[v]:
        if visited[i] == 0: #방문하지 않았으면
            dfs(graph, i, visited) #재귀문을 통해서 dfs 수행
    return True 

dfs(graph, 1, visited) #1번 컴퓨터부터 dfs 실행하기
print(sum(visited)-1)	# 방문한 컴퓨터 개수 - 1번 컴퓨터