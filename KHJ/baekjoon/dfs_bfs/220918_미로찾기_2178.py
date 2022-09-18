def solution(maze, dst):
    max_count = dfs([0,0], 1, maze, dst, dst[0]*dst[1])
    return min_count
    

def dfs(now, count, maze, dst, min_count):
    move = [[1,0], [0,1], [0,-1], [-1,0]]
    for i in range(4):
      new = [now[0]+move[i][0], now[1]+move[i][1]]
      if now == dst:
        # print()
        # print(count, arr[dst[0]][dst[1]])
        # print()
        # if count < arr[dst[0]][dst[1]]:
        if count < max_count:
           return count
      if 0<=new[0]<=dst[0] and 0<=new[1]<=dst[1] and maze[new[0]][new[1]] == 1:
        maze[new[0]][new[1]] = 2
        max_count = dfs(new, count+1, maze, dst, max_count)
    return min_count

    
# def select_dfs_max(maze, dst):
#     count_arr = []
#     stack = [[0,0,0]]
#     move = [[1,0], [1,0], [0,-1], [-1,0]]
#     while len(stack) != 0:
#         print(stack)
#         now = stack.pop()
#         count = now[2]
#         if now[:2] == dst:
#             count_arr.append(now[2])
#         else:
#             for i in range(4):
#                 new = [now[0]+move[i][0], now[1]+move[i][1], count+1]
#                 if 0<=new[0]<=dst[0] and 0<=new[1]<=dst[1] and maze[new[0]][new[1]] == 1:
#                     stack.append(new)
    
#     return max(count_arr)         

        
# N, M = list(map(int, input().split(" ")))
# arr = []
# for i in range(N):
#     input_ = input()
#     tmp = [1 if x == "1" else 0 for x in input_]
#     arr.append(tmp)
# arr[N-1][M-1] = N*M
# print(solution(arr, [N-1,M-1]))

N = 4
M = 7
arr = [[1,0,1,1,1,1], [1,0,1,0,1,0], [1,0,1,0,1,1], [1,1,1,0,1,1]]
arr = [[1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1],[1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1]]
arr = [[1,0,1,1,1,1,1],[1,1,1,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
arr = [[1,1,1,0,1,1,1], [1,0,1,1,1,0,1], [1,0,0,0,0,0,1], [1,1,1,1,1,1,1]]
arr[N-1][M-1] = N*M
print(solution(arr, [N-1,M-1]))



# 이거 아마 bfs로 하는게 맞을거같고
# bfs 쓰려면 collections.dequeue 써야함 