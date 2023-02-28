import sys
input = sys.stdin.readline

# N = int(input())
# numbers = input().rstrip()
# arr = [int(x) for x in numbers]

# print(sum(arr))

N = int(input())
numbers = list(input())
sum = 0

for i in numbers:
    sum += int(i)

print(sum)
