
def solution3(total_sugar):
    five = 0
    three = 5001
    total = five + three
    while five*5 < total_sugar:
        div, mod = divmod((total_sugar - five*5), 3)
        if mod == 0 and five + div < total:
            three = div
            total = five + three
        five += 1
        
    if total == 5001:
        return -1
    return total

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
    
    
# total_sugar = int(input())
# solution2(total_sugar)


N = int(input())
print(solution3(N))