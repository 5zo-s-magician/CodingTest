import sys
input = sys.stdin.readline

min, max = map(int, input().split())

good = [1] * (max-min+1)
answer = 0

if min == 1:
    answer += 1

for i in range(2, int(max**0.5)+1):
    pow = i*i
    for j in range(min//pow, max//pow+1):
        idx = pow*j-min
        if idx <0:
            continue
        good[j*pow-min] = 0
        
print(sum(good))