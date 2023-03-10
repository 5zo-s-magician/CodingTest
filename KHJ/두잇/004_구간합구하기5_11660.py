from re import L
import sys
input = sys.stdin.readline

# 각 줄별 더하기
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
arr[0] = [0] * (N+1)

for i in range(1,N+1):
    arr[i] = [0] + list(map(int, input().split()))
    
    
for i in range(1,N+1):
    for j in range(1,N+1):
        arr[i][j] += arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1]

for i in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    answer = arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1]
    print(answer)
