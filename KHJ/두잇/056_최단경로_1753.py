#-*- coding:utf-8 -*-
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 인접리스트, 거리 리스트 인풋 받고
# 거리 리스트는 시작 = 0으로
# now -> 인접리스트의 거리 계산
# 인접 리스트를 queue로? queue를 우선순위 큐로 구현하면 무조건 젤 작은게 골라진다구? + visited도 해야하네!
# 충분히 큰 수는? 

V, E = map(int,input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
distance = [sys.maxsize] * (V+1)
visited = [False] * (V+1)
distance[start] = 0
queue = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w,v))

heappush(queue, (0,start))

while queue:
    now = heappop(queue)[1]
    if visited[now]:
        continue
    visited[now] = True
    for x in graph[now]:
        next = x[1]
        w = x[0]
        distance[next] = min(distance[next], distance[now]+w)
        heappush(queue, (distance[next], next))
        
for x in distance[1:]:
    if x == sys.maxsize:
        print("INF")
    else:
        print(x) 
    

# #-*- coding:utf-8 -*-
# import sys
# from queue import PriorityQueue
# input = sys.stdin.readline

# V, E = map(int,input().split())
# start = int(input())
# graph = [[] for _ in range(V+1)]
# distance = [sys.maxsize] * (V+1)
# visited = [False] * (V+1)
# distance[start] = 0
# queue = PriorityQueue()

# for _ in range(E):
#     u, v, w = map(int, input().split())
#     graph[u].append((w,v))

# queue.put((0,start))

# while queue.qsize()>0:
#     now = queue.get()[1]
#     if visited[now]:
#         continue
#     for x in graph[now]:
#         next = x[1]
#         w = x[0]
#         distance[next] = min(distance[next], distance[now]+w)
#         queue.put((distance[next], next))
        
# for x in distance[1:]:
#     if visited:
#         print(x)
#     else:
#         print("INF")
    
