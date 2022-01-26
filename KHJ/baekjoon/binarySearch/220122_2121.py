def input_cutter(input_):
    input_splitted = input_.split()
    point_count = int(input_splitted[0])
    garo, sero = int(input_splitted[1]), int(input_splitted[2])
    input_splitted = input_splitted[3:]
    points = []
    for i in range(point_count):
        points.append([int(input_splitted[2*i]), int(input_splitted[2*i+1])])
    return point_count, int(garo), int(sero), points

def solution(point_count, garo,sero, points):
    answer = 0
    for point in points:
        if [point[0],point[1]+sero] in points:
            if [point[0]+ garo,point[1]] in points:
                if [point[0]+garo,point[1]+sero] in points:
                    answer += 1
    return answer


point_count = input()
point_count = int(point_count)
garo, sero = input().split()
points = []
for i in range(point_count):
    point = list(map(int,input().split()))
    points.append(point)

print(solution(point_count, int(garo),int(sero), points))