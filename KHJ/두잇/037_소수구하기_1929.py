import sys
input = sys.stdin.readline

start, end = map(int,input().split())
arr = [0] * (end+1)
for i in range(2,end+1):
    arr[i] = i

for i in range(2, int(end**(0.5)+1)):
    if arr[i] == 0:
        continue
    for j in range(i+i, end+1, i):
        arr[j] = 0

for i in range(start, end+1):
    if arr[i] != 0:
        print(arr[i])