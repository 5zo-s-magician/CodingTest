import sys
input = sys.stdin.readline

N = int(input())
stack = []
targets = []
answer = []
no = False
for i in range(N):
    targets.append(int(input()))

t = targets.pop(0)
s = -1
for i in range(1, N+1):
    if t == s:
        while t == s:
            stack.pop()
            if stack:
                s = stack[-1]
            else:
                s = -1
            answer.append("-")
            t = targets.pop(0)
            
    if t > s:
        stack.append(i)
        s = i
        answer.append("+")

    if t < s:
        print("NO")
        no = True
        break

if not no:
    for x in answer:
        print(x)
    for i in range(len(stack)):
        print("-")