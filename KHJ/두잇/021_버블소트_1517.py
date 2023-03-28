import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

result = 0
tmp = [0]*N

def merge_sort(s, e):
    global result
    if e-s<1:
        return
    m = (s+e)//2
    merge_sort(s, m)
    merge_sort(m+1, e)
    for i in range(s,e+1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m+1
    while index1<m+1 and index2 < e+1:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            if index2-k>0:
                result += index2 - k
            index2 += 1
            k += 1
        else:
            A[k] = tmp[index1]
            if index1-k>0:
                result += index1 - k
            index1 += 1
            k += 1
    while index1<m+1:
        A[k] = tmp[index1]
        if index1-k>0:
            result += index1 - k
        index1 += 1
        k += 1
    
    while index2<e+1:
        A[k] = tmp[index2]
        if index2-k>0:
            result += index2 - k
        index2 += 1
        k += 1

merge_sort(0,N-1)

print(result)
