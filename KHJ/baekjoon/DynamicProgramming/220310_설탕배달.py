def solution1(total_sugar):
    three = 0
    five = 0
    while total_sugar>=0:
        if total_sugar % 5 == 0:
            five = total_sugar//5
            print(three+five)
            return
        else:
            three += 1
            total_sugar -= 3
    print(-1)

def solution2(total_sugar):
    dp = [-1]*(total_sugar+6)
    dp[3] = 1
    dp[5] = 1
    for i in range(6,total_sugar+1):
        if dp[i-3] != -1:
            dp[i] = dp[i-3] + 1
        if dp[i-5] != -1:
            if dp[i] == -1:
                dp[i] = dp[i-5] +1
            else:
                dp[i] = min(dp[i], dp[i-5] + 1)
    print(dp[total_sugar])
    return 
    
    
total_sugar = int(input())
solution2(total_sugar)