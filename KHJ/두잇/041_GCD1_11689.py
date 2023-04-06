N = int(input())
arr = [x for x in range(N+1)]

for i in range(2, (N**(0.5)) + 1):
    if arr[i] == i:
        for j in range(1, N//i + 1):
            arr[i*j] = arr[i*j] - arr[i*j]//i

print(arr[N])