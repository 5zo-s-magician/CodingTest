import sys
input = sys.stdin.readline

exp_minus = input().split("-")

for i,x in enumerate(exp_minus):
    arr_plus = x.split("+")
    exp_minus[i] = (-1)*sum(map(int, arr_plus))
    if i == 0:
        exp_minus[i] *= (-1)

print(sum(exp_minus))
