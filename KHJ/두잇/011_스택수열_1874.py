import sys
input = sys.stdin.readline

N = int(input())
stack = []
targets = []
answer = []
no = False
for i in range(N):
    targets.append(int(input()))

n = 1
for i in range(N):
    t = targets.pop(0)
    
    if n <= t:
        while n <= t:
            stack.append(n)
            n += 1
            answer.append("+")
        stack.pop()
        answer.append("-")
    
    elif n > t:
        if stack and stack[-1] == t:
            stack.pop()
            answer.append("-")
        else:
            no = True
            print("NO")
            break

if not no:
    for x in answer:
        print(x)