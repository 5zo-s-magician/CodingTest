import sys
input = sys.stdin.readline
end = 10000000

arr = [i for i in range(end+1)]
arr[1] = -1

for i in range(2, end+1):
    if arr[i] == -1:
        continue
    for j in range(2, end//i + 1 ):
        arr[i*j] = -1

N = int(input())

for x in arr[N:]:
    if x== -1:
        continue
    elif str(x) == str(x)[::-1]:
        print(x)
        break



    