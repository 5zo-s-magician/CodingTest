# import sys
# input = sys.stdin.readline

# A, B = map(int, input().split())
# start = int(A**(0.5))
# end = int(B**(0.5))
# print(start, end)

# arr = [x for x in range(0, end+1)]
# answer = 0
# if start == 1:
#     answer += 1

# for i in range(2, end+1):
#     if arr[i] == -1:
#         continue
#     elif i >= start:
#         answer += 1
#     for j in range(2, end//i+1):
#         arr[i*j] = -1

# print(answer)
        
        
        
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
start = int(A**(0.5))
end = int(B**(0.5))

arr = [x for x in range(0, end+1)]
answer = 0

for i in range(2, end+1):
    if arr[i] == -1:
        continue
    for j in range(2, end//i+1):
        arr[i*j] = -1

for x in arr[2:]:
    if x == -1:
        continue
    i = 2
    while True:
        if A <= x**i <= B:
            answer += 1
        elif x**i > B:
            break
        i += 1
print(answer)
        