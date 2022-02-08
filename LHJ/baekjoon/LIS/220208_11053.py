length = int(input())

array = [0 for i in range(length)]

# for i in range(0, length):
array = map(int, input().split())
array = list(array)

lower_bound = [array[0]]
answer = 1

for value in array:
    if(lower_bound[-1] < value):
        lower_bound.append(value)
    else:
        for num in range(0, len(lower_bound)):
            if(lower_bound[num] > value or lower_bound[num] == value):
                lower_bound[num] = value
                break
    # print(lower_bound)

answer = len(lower_bound)

print(answer)
