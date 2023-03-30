import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
answer = 0

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def DFS(friend):
    global answer
    if len(friend) == 5:
        answer = 1
        return 
    else:
        for x in graph[friend[-1]]:
            if x not in friend:
                DFS(friend+[x])


for i in range(N):
    DFS([i])
    if answer == 1:
        break

print(answer)