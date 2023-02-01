def count(a, b):
    arr = [[0 for i in range(b+1)] for i in range(a+1)]
    for i in range(1,b+1):
        arr[0][i] = i
    for x in range(1,a+1):
        for y in range(1,b+1):
            if y==1:
                arr[x][y] = 1
            else:
                arr[x][y] = arr[x][y-1] + arr[x-1][y]
    
    return arr[a][b]

T = int(input())
for i in range(T):
    print(count(int(input()), int(input())))
