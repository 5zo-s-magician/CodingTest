from ast import Num
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
same = [0] * M
answer = 0

for i in range(1,N):
    arr[i] += arr[i-1]

for i in range(N):
    m = arr[i] % M
    if m == 0:
        answer += 1
    same[m] += 1

for i in range(M):
    answer += same[i]*(same[i]-1)//2

print(answer)


