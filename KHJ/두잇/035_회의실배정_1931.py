import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
arr = []
answer = 0
end = -1

for i in range(N):
    a, b = map(int, input().split())
    heappush(arr, [b, a])

for _ in range(N):
    # 짧은거 우선 배치
    x = heappop(arr)
    if x[1] >= end:
        answer += 1
        end = x[0] 

print(answer)




# import sys
# from heapq import heappop, heappush
# input = sys.stdin.readline

# N = int(input())
# arr = []
# answer = []

# for i in range(N):
#     a, b = map(int, input().split())
#     heappush(arr, [b-a+1, a, b])

# def include(target, comp):
#     if target[1] <= comp[1] <= target[2]:
#         return True
#     if target[1] <= comp[2] <= target[2]:
#         return True
#     if target[1] >= comp[1] and target[2] <= comp[2]:
#         return True
#     return False

# for _ in range(N):
#     # 짧은거 우선 배치
#     x = heappop(arr)
#     is_include = False
#     for y in answer:
#         if include(y, x):
#             is_include = True
#     if not is_include:
#         answer.append(x)

# print(answer)
# print(len(answer))

