import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

# 1. get combination
D = [[0 for i in range(N+M+2)] for j in range(N+M+2)]

for i in range(N+M+2):
    for j in range(i+1):
        if j == 0 or j == i:
            D[i][j] = 1
        else:
            D[i][j] = D[i-1][j] + D[i-1][j-1]
            if D[i][j] > 1000000000:
                D[i][j] = 1000000001

if D[N+M][M] < K:
    print(-1)
else:
    while not (N==0 and M==0):
        if D[N-1+M][M] >= K:
            print("a", end="")
            N -= 1
        else:
            print("z", end="")
            K -= D[N-1+M][M]
            M -= 1
