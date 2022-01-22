n = input()
width, height = input().split()

width = int(width)
height = int(height)
x_sort = []
y_sort = []

point_dic = {}

answer = 0

for i in range(0, int(n)):
    x, y = input().split()
    x_sort.append([int(x), int(y)])
    y_sort.append([int(x), int(y)])
    if int(x) in point_dic:
        point_dic[int(x)].append(int(y))
    else:
        point_dic[int(x)] = [int(y)]

point_dic = sorted(point_dic)
point_list = list(point_dic)


x_sort.sort(key=lambda x: (x[0], x[1]))
y_sort.sort(key=lambda x: (x[1], x[0]))
print(point_dic)

# print(x_sort)
# print(y_sort)

for point in x_sort:
    tmp_x_min = point[0] #point[0]이 key값인 list의 index값
    tmp_x_max = point_list[-1] #point_list[-1]의 index값
    # for i in range(0, 21):
        # if()
    # if([point[0]+width, point[1]] in x_sort):
    #     if([point[0]+width, point[1]+height] in x_sort):
    #         if([point[0], point[1]+height] in x_sort):
    #             answer += 1

    # for i in range(0, 21): #(point[0]+width, point[1])

print(answer)

# print(point)