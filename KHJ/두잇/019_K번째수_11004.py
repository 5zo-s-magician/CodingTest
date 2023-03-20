import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

def sort(i, j):
    global A
    if i< 0 or j<0 or i >= j:
        return
    
    pivot = A[j]
    start = i
    end = j-1
    
    while start <= end:
        if pivot > A[start]:
            start += 1
        elif pivot < A[start]:
            A[start], A[end] = A[end], A[start]
        if pivot < A[end]:
            end -= 1
    
    A[end+1], A[j] = A[j], A[end+1]
    
    sort(0, end)
    sort(end+2, j)
        
sort(0,N-1)

print(A[K-1])    

