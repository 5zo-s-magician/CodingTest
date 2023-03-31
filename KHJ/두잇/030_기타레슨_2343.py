import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

s = max(arr)
e = sum(arr)

while s <= e:
    m = (s+e)//2
    sum_ = 0
    count = 0
    for i in range(N):
        if sum_+ arr[i] > m:
            count += 1
            sum_ = 0
        sum_ += arr[i]
    if sum !=0:
        count += 1
    if count>M:
        s = m+1
    else:
        e = m-1

print(s)
        
        
            
