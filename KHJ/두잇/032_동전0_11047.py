import sys
input = sys.stdin.readline

N, target = map(int, input().split())
arr = [0]*N 
answer = 0

for i in range(N):
    arr[N-i-1] = int(input())

for i in range(N):
    if target == 0:
        break
    
    div, mod = divmod(target, arr[i])
    answer += div
    target = mod
    
print(answer)