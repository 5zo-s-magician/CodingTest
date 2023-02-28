# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# arr = [0] + list(map(int, input().split()))
# part_sum_arr = [0]*len(arr)
# part_sum_arr[1] = arr[1]
# for i in range(1, len(arr)):
#     part_sum_arr[i] = part_sum_arr[i-1] + arr[i]
# for _ in range(M):
#     start, end = map(int, input().split())
#     print(part_sum_arr[end]-part_sum_arr[start-1])
    
# # N, M = map(int,input().split())
# # arr = [0]+list(map(int, input().split()))
# # for _ in range(M):
# #     start, end = map(int, input().split())
# #     print(sum(arr[start:end+1]))

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
s = [0] * (N+1)

for i in range(1,len(arr)+1):
    s[i] = s[i-1] + arr[i-1]

for k in range(M):
    i, j = map(int, input().split())
    
    print(s[j]-s[i-1])




