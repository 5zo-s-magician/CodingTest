import sys
input = sys.stdin.readline

def gcd(a,b):
    if b>a:
        a, b = b, a
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    g = gcd(a,b)
    answer = g * (a//g) * (b//g)
    print(answer)