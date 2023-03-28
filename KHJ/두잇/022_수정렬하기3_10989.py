import sys
input = sys.stdin.readline

N = int(input())
num = [0]*(100001)

for i in range(N):
    num[int(input())] += 1

for i in range(100001):
    while num[i] > 0:
        print(i)
        num[i] -= 1

