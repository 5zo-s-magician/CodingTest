def solution(arr):
    dp = [1 for i in range(len(arr))]
    for i in range(1, len(dp)):
      max_ = 0
      for j in range(1, i):
        if arr[j] < arr[i] and dp[j] > max_:
          max_ = dp[j]
        dp[i] = max_+1
    return max(dp)


N = int(input())
arr = list(map(int, input().split()))
arr = [0] + arr
print(solution(arr))