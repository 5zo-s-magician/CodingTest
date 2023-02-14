import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
#val_arr = [i for i in range(m+1)]
parent = [i for i in range(n+1)]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a>b:
        a,b = b,a
    
    parent[b] = a
    
def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
    


for i in range(m):
    uf, a, b = map(int, input().split())
    if uf == 0:
        # union
        union(a, b)
    if uf == 1:
        a = find(a)
        b = find(b)
        if a==b:
            print("YES")
        else:
            print("NO")