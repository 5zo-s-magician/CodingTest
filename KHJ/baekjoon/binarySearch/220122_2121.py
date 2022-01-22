def input_cutter(input_):
    print(input_)
    input_line_cutted = input_.split("\n")
    point_count = int(input_line_cutted.pop(0))
    garo, sero = input_line_cutted.pop(0).split()
    points = []
    for i in range(len(input_line_cutted)):
        a, b = input_line_cutted[i].split()
        points.append([int(a), int(b)])
    return point_count, int(garo), int(sero), points

def solution(point_count, garo,sero, points):
    answer = 0
    for point in points:
        if [point[0],point[1]+sero] in points:
            if [point[0]+ garo,point[1]] in points:
                if [point[0]+garo,point[1]+sero] in points:
                    answer += 1
    return answer
    


a = """6
2 3
0 0
2 0
2 3
0 3
4 0
4 3"""
point_count, garo,sero, points = input_cutter(a)
print(solution(point_count, garo,sero, points))