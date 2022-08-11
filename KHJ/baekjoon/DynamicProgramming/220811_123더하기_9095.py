def solution(N):
    DP = [0]*(N+3)
    DP[1] = 1
    DP[2] = 2
    DP[3] = 4
    for i in range(4,N+1):
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
    return DP[N]

count = int(input())
answer = [0] * count
for k in range(count):
    N = int(input())
    answer[k] = solution(N)

for k in range(count):
    print(answer[k])

        
    