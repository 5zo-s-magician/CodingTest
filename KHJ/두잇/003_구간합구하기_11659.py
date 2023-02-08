import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
part_sum_arr = [0]*len(arr)
part_sum_arr[1] = arr[1]
for i in range(1, len(arr)):
    part_sum_arr[i] = part_sum_arr[i-1] + arr[i]
for _ in range(M):
    start, end = map(int, input().split())
    print(part_sum_arr[end]-part_sum_arr[start-1])
    
# N, M = map(int,input().split())
# arr = [0]+list(map(int, input().split()))
# for _ in range(M):
#     start, end = map(int, input().split())
#     print(sum(arr[start:end+1]))