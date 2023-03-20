# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = list(map(int, input().split()))
# answer = 0

# for i in range(N):
#     m = 1001
#     idx = -1
#     for j in range(i,N):
#         if arr[j] < m:
#             m = arr[j]
#             idx = j
#     answer += sum(arr[0:i]) + m
#     arr[i], arr[idx] = arr[idx], arr[i]
    
    
# print(answer)

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = [0] * N
answer = 0

for i in range(1,N):
    insert_point = i
    insert_value = A[i]
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insert_point = j+1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value

S[0] = A[0]

for i in range(1,N):
    S[i] = S[i-1] + A[i]

sum = 0 

for i in range(0,N):
    answer += S[i]

print(answer)
            