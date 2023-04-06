import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def gcd(a,b):
    if a<b:
        a, b = b, A
    while b != 0:
        a, b = b, a % b
    return a

answer = str(1) * gcd(A, B)

print(answer)