import sys
sys.setrecursionlimit(10**6)

N = int(input())

def isPrime(N):
    for i in range(2,N//2+1):
        if N % i == 0:
            return False
    return True


def DFS(num):
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(1, 10, 2):
            if isPrime(num*10 + i):
                DFS(num*10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)