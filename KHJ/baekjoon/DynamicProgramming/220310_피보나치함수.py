def solution(number):
    dp = [0,0] * (number+2)
    dp[0] = [1,0]
    dp[1] = [0,1]
    for i in range(2,number+1):
        dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1]+dp[i-2][1]]
    return dp
    
count = int(input())
numbers = []
results = []
for i in range(count):
    number = int(input())
    # result = solution(number)
    # results.append(result)
    numbers.append(number)

dp = solution(max(numbers))
for number in numbers:
    print(str(dp[number][0])+" "+str(dp[number][1]))