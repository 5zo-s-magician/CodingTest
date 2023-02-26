# 1. deque
from collections import deque
a = deque()
a.append()
a.appendleft()
a.pop()
a.popleft()

# 2. heapq
from heapq import heappop, heappush
a = []
heappop(a)
heappush(a, 1)

# sys
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
sys.maxsize

# 기타
arr = []
str.replace("a", "b")
arr[::-1] 
s1 = set()
s1.intersaction(s2)
s1.union(s2)

# 행렬 전치
A = [[1,2,3], [4,5,6]]
B = [list(x) for x in zip(*A)]