import sys
from heapq import heappop, heappush
input = sys.stdin.readline

V, E = map(int,input().split())
edge_graph = []
parent = [i for i in range(V+1)]

for _ in range(E):
    a, b, c = map(int,input().split())
    heappush(edge_graph,(c,a,b))

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def find(a):
    if parent[a]==a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

userEdge = 0
result = 0

while userEdge<V-1:
    w, a, b = heappop(edge_graph)
    if find(a) != find(b):
        union(a,b)
        userEdge += 1
        result += w

print(result)