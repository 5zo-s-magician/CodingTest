import sys
from heapq import heapify, heappop, heappush
from queue import PriorityQueue

input = sys.stdin.readline

# 1은 다 더해주기
# 0 개수 세어놓기
# 음수는 음수끼리
# 음수남으면 0이랑
# 안되면 그냥 더하기
# 양수는 그냥 큰거끼리 묶으면 됨

N = int(input())
plus_arr = PriorityQueue()
minus_arr = PriorityQueue()
answer = 0
one = 0
zero = 0

for _ in range(N):
    x = int(input())
    if x == 1:
        one += 1
    elif x == 0:
        zero += 1
    elif x<0:
        minus_arr.put(x)
    else:
        plus_arr.put(-x)

# 음수는 음수끼리!
while minus_arr.qsize() > 1:
    a = minus_arr.get()
    b = minus_arr.get()
    answer += a*b

if minus_arr.qsize() != 0:
    if zero != 0:
        minus_arr.get()
    else:
        answer += minus_arr.get()

# 양수는 양수끼리!
while one != 0:
    answer += 1
    one -= 1

while plus_arr.qsize() > 1:
    a = plus_arr.get()
    b = plus_arr.get()
    answer += a*b

if plus_arr.qsize() != 0:
    answer += (-1) * plus_arr.get()


print(answer)