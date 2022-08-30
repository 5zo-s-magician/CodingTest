def solution(arr, N):
    for i in range(1, N):
        arr[i] = max(arr[i-1]+arr[i], arr[i])
    return max(arr)

N = int(input())
arr = list(map(int, input().split()))
print(solution(arr, N))