import sys 
input = sys.stdin.readline

N = int(input())
M = int(input())
ingre = list(map(int, input().split()))
ingre.sort()
start = 0
end = N-1
answer = 0

while start<end:
    sum_ = ingre[start] + ingre[end]
    if sum_ > M:
        end -= 1
    elif sum_ < M:
        start += 1
    else:
        start += 1
        answer += 1

print(answer)