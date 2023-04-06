import sys
from collections import deque
input = sys.stdin.readline

A, B, C = map(int, input().split())
div = deque()

def gcd(a,b):
    if a<b:
        a, b = b, a
    div.append(0)
    while b != 0:
        div_, mod_ = divmod(a, b)
        div.append(div_)
        a, b = b, mod_
    return a

g = gcd(A, B)
if C % g != 0:
    print(-1)
else:
    tmp = C//g
    x=1
    y=0
    while div:
        q = div.pop()
        x, y = y, x-y*q
    
    x *= tmp
    y *= tmp
    print(x,y)
        
    
    
    