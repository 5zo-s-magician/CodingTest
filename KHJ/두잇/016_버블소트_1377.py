# import sys
# input = sys.stdin.readline

# N = int(input())
# A = [0] * N
# for i in range(N):
#     A[i] = int(input())

# changed = False
# for i in range(N):
#     changed = False
#     for j in range(N-i-1):
#         if A[j] > A[j+1]:
#             change = True
#             A[j], A[j+1] = A[j+1], A[j]
#     if not change:
#         print(i)
#         break


import sys
input = sys.stdin.readline

N = int(input())
A = []
for i in range(N):
    A.append([int(input()), i])

A.sort()

max_distance = 0

for i in range(N):
    distance = A[i][1] - i
    if distance > max_distance:
        max_distance = distance
        
print(max_distance + 1)
