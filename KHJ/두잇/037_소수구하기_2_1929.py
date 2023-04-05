import sys
input = sys.stdin.readline

M, N = map(int, input().split())

arr = [1]*(N+1)
arr[0] = -1
arr[1] = -1

# 소수를 찾을 땐, traverse 해서 나누기보단
# for i in range(len(arr)):
#     x = arr[i]
#     if x == -1:
#         continue
#     elif x >= M :
#         print(x)
#     for j in range(i+1, len(arr)):
#         if arr[j] == -1:
#             continue
        
#         if arr[j] % x == 0:
#             arr[j] = -1

# 배수를 구해서 바로 때려버리는게 훨씬 빠르다!
for i in range(len(arr)):
    if arr[i] == -1:
        continue
    elif i >= M:
        print(i)
    for j in range(2, N//i+1):
        arr[i*j] = -1

