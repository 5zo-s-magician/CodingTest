# -*- coding: utf-8 -*-

import sys
read = sys.stdin.readline

test_case = int(input())

for case in range(0, test_case):
    m, n, k = map(int, input().split())
    answer = 0

    field = [[0] * (m) for _ in range(n)]  #해당 좌표에 배추가 있는지
    graph = [[0] * (m) for _ in range(n)] #해당 좌표에 몇번 애벌래가 있는지

    for _ in range(k):
        a, b = map(int, read().split())
        field[a][b] = 1 # 배추 심음

    for i in range(0, len(field[0])):
        for j in range(0, len(field)):
            try:
                if(field[i][j] == 1): #만약 배추가 있으면
                    if(field[i][j-1] == 0 and field[i-1][j] == 0):
                        answer += 1
                        graph[i][j] == answer
                # elif(field[i][j-1] == 1):
                #     graph
            except:
                pass
    
    print(answer)
