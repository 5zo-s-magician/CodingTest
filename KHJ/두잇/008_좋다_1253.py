# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# answer = 0

# for k in range(N):
#     find = arr[k]
#     i = 0
#     j = N-1
#     while i<j:
#         if find == arr[i] + arr[j]:
#             if i != k and j != k:
#                 answer += 1
#                 break
#             if i == k:
#                 i += 1
#             if j == k:
#                 j -= 1
#         elif find > arr[i] + arr[j]:
#             i += 1
#         else:
#             j -= 1

# print(answer)



# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = list(map(int, input().split()))
# arr.sort(reverse=True)
# answer = 0

# for i in range(len(arr)):
#     flag = False
#     now = arr[i]
#     for j in range(i+1, len(arr)-1):
#         for k in range(j+1, len(arr)):
#             if now == arr[j] + arr[k]:
#                 answer += 1
#                 flag = True
#                 break
#         if flag:
#             break

# print(answer)

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0

for idx, target in enumerate(arr):
    start = 0
    end = N-1
    while start < end:
        sum_ = arr[start]+arr[end]
        if sum_ == target:
            if start != idx and end != idx:
                answer += 1
                break
            if start == idx:
                start += 1
            if end == idx:
                end -= 1
        elif sum_ < target:
            start += 1
        else:
            end -= 1
            
print(answer)