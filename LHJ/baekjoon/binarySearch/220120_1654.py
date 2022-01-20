k, n = input().split()
line_length = []

for i in range(0, int(k)):
    line_length.append(int(input()))

# min_val = min(line_length)
min_val = 1
max_val = max(line_length)

result = 0
answer = (min_val+max_val)//2

for j in range(0, 120):
    # print(answer)
    for i in line_length:
        result += i//answer

    if(result > int(n) or result == int(n)):
        min_val = answer
        answer = (answer+max_val)//2
    else:
        max_val = answer
        answer = (answer+min_val)//2
    result = 0


for i in line_length:
    result += i //(answer+1)

if(result == int(n)):
    answer += 1
    
print(answer)