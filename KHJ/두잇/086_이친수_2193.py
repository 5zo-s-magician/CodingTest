import sys
input = sys.stdin.readline

N = int(input())
s = [0] * (N+1)
s[0] = 1
s[1] = 1

for i in range(2,N+1):
    s[i] = s[i-1] + s[i-2]

print(s[N-1])