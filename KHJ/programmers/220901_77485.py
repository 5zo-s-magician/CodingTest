import numpy as np

def print_arr(arr):
    a = np.array(arr)

    for line in a:
        print ('  '.join(map(str, line)))


def solution(rows, columns, queries):
    answer = []
    arr = [[(j*columns)+i for i in range(1,columns+1)] for j in range(rows)]
    arr_cmp = [[(j*columns)+i for i in range(1,columns+1)] for j in range(rows)]
    for query in queries:
        points = [[query[0]-1, query[1]-1],[query[0]-1, query[3]-1], [query[2]-1, query[3]-1], [query[2]-1, query[1]-1]]
        
        # for i in range(points[0][1]+1, points[1][1]+1):
        #     arr[points[0][0]][i] -= 1
            
        # for i in range(points[1][0]+1, points[2][0]+1):
        #     arr[i][points[1][1]] -= columns
        
        # for i in range(points[3][1], points[2][1]):
        #     arr[points[2][0]][i] += 1
        
        # for i in range(points[0][0], points[3][0]):
        #     arr[i][points[0][0]] += columns
        
        save = arr[points[0][0]][points[0][1]]
        
        for i in range(points[0][0], points[3][0]):
            arr[i][points[0][0]] = arr[i+1][points[0][0]]
            
        for i in range(points[3][1], points[2][1]):
            arr[points[2][0]][i] = arr[points[2][0]][i+1]
            
        for i in reversed(range(points[1][0]+1, points[2][0]+1)):
            arr[i][points[1][1]] = arr[i-1][points[1][1]]
        
        for i in reversed(range(points[0][1]+1, points[1][1]+1)):
            arr[points[0][0]][i] = arr[points[0][0]][i-1]
            
        arr[points[0][0]][points[0][1]+1] = save    
        
        
        print_arr(arr)
    for i in range(columns):
        for j in range(rows):
            if arr_cmp[j][i] != arr[j][i]:
                answer.append(arr[j][i]) 

    return sorted(answer)

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
solution(rows, columns, queries)