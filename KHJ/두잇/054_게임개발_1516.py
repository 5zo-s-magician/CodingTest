import sys
from collections import deque
input = sys.stdin.readline

# 1. input
N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
time = [0] * (N+1)
answer = [0] * (N+1)
dq = deque()

for i in range(1,N+1):
    tmp = list(map(int, input().split()))
    time[i] = tmp[0]
    for x in tmp[1:-1]:
        graph[x].append(i)
    indegree[i] = len(tmp[1:-1])

for i in range(1,N+1):
    if indegree[i] == 0:
        dq.append(i)
        
while dq:
   now = dq.popleft()
   for next in graph[now]:
       indegree[next] -= 1
       answer[next] = max(answer[next], answer[now]+ time[now])
       if indegree[next] == 0:
           dq.append(next)

for i in range(1,N+1):
    print(answer[i] + time[i])
