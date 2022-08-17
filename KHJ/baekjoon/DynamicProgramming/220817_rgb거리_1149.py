def solution(arr, N):
    for i in range(1,N+1):
        arr[i][0] = min(arr[i][0] + arr[i-1][1], arr[i][0] + arr[i-1][2])
        arr[i][1] = min(arr[i][1] + arr[i-1][2], arr[i][1] + arr[i-1][0])
        arr[i][2] = min(arr[i][2] + arr[i-1][0], arr[i][2] + arr[i-1][1])
    return min(arr[N])

N = int(input())
arr = [[0]*3]*(N+1)
for i in range(N):
    tmp = list(map(int, input().split()))
    arr[i] = tmp
print(solution(arr,N))