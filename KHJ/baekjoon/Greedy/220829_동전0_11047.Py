def solution(arr, money):
    answer = 0
    for i in reversed(range(len(arr))):
        div, mod = divmod(money, arr[i])
        answer += div
        money = mod
    return answer

N, money = list(map(int, input().split()))
arr = [0 for i in range(N)]
for i in range(N):
    arr[i] = int(input())

print(solution(arr, money))