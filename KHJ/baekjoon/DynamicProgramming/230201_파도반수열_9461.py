def padoban(n):
    DP = [0,1,1,1,2,2] + [0] * 95
    for i in range(6,n+1):
        DP[i] = DP[i-5] + DP[i-1]
    
    return DP[n]

num = int(input())
for i in range(num):
    n = int(input())
    print(padoban(n))
    
    