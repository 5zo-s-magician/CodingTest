import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
avgs_1 = sum(scores)/N
M = max(scores)
new_scores = [x/M*100 for x in scores]

print(sum(new_scores)/N)