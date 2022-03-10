# DP 는 Bottom UP 방식이라는걸 잘 생각하면 풀 수 있음!
# 숫자 1에서부터 주어진 숫자까지 가는 횟수를 array에 기록!!!

# def solution(number):
#     d = [0 for i in range(number+1)]
#     for i in range(2, number+1):
#         d[i] = d[i-1] +1;
#         if i%2 == 0:
#            d[i] = min(d[i//2] + 1, d[i])
#         if i%3 == 0:
#             d[i] = min(d[i//3] + 1, d[i])    
#     print(d[number])
#     return d[number]

# number = int(input())
# solution(number)


def solution(number):
    dp = [10000000]*(number+1)
    dp[1] = 0
    for i in range(2,number+1):
        if i%3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)
        if i%2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)
        dp[i] = min(dp[i], dp[i-1]+1)
    print(dp[number])
    return
    
number = int(input())
solution(number)