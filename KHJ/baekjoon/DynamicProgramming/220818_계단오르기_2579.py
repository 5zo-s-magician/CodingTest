def getMaxStairSum(stairs, N):
    dp = [0 for i in range(N+1)]
    for i in range(1, N+1):
        if i == 1:
            dp[1] = stairs[1]
        elif i == 2:
            dp[2] = stairs[1]+stairs[2]
        else:
            dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])
    return dp[len(stairs)-1]

N = int(input())
stairs = [0 for i in range(N+1)]
for i in range(1, N+1):
  stairs[i] = int(input())

print(getMaxStairSum(stairs, N))