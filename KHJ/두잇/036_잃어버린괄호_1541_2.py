import sys
input = sys.stdin.readline

eq = input().rstrip()
nums = eq.split("-")

answer = sum(list(map(int, nums[0].split("+"))))
nums = nums[1:]

for x in nums:
    nums_plus = list(map(int, x.split("+")))
    summ = sum(nums_plus)
    answer -= summ

print(answer)