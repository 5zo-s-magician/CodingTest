import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())

plus_heap = []
minus_heap = []

for i in range(N):
    n = int(input())
    if n == 0:
        if not plus_heap and not minus_heap:
            print(0)
        elif not plus_heap:
            m = heappop(minus_heap)
            print(-m)
        elif not minus_heap:
            p = heappop(plus_heap)
            print(p)
        else:     
            if plus_heap[0] >= minus_heap[0]:
                m = heappop(minus_heap)
                print(-m)
            else:
                p = heappop(plus_heap)
                print(p)
    elif n > 0:
        heappush(plus_heap, n)
    else:
        heappush(minus_heap, -n)

# 우선순위 큐
from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdout.readline

myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print("0\n")
        else:
            temp = myQueue.get():
                print(str(temp[1])+"\n")
    else:
        myQueue.put((abs(request), request))
            
