def solution(arr):
    for i in reversed(range(0,len(arr)-1)):
        for j in range(0, len(arr)-i):
            arr[i][j] += max(arr[i+1][j], arr[i+1][j+1])
    return arr[0][0]

N = int(input())
arr = [[0 for i in range(N)] for j in range(N)]
arr[0][0] = int(input())
for i in range(1,N):
    arr[i][0:i+1] = list(map(int, input().split()))