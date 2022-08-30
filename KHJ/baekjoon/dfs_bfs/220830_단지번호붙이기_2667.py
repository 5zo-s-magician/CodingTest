def solution(arr, N):
      count = 0
  count_arr = []
  for i in range(N):
    for j in range(N):
      if arr[i][j] == 1:
        count += 1
        arr, count_ = dfs(arr, i, j, N)
        count_arr.append(count_)
  return count, count_arr

def dfs(arr, i, j, N):
  stack = [[i, j]]
  count = 0
  while len(stack)>0:
    #print(stack)
    a, b = stack.pop()
    if arr[a][b] == 1:
      if b-1>=0 and [a, b-1] not in stack:
         if arr[a][b-1] == 1:
            stack.append([a, b-1])
      if a-1>=0 and [a-1, b] not in stack:
        if arr[a-1][b] == 1:
          stack.append([a-1, b])
      if a+1 < N and [a+1, b] not in stack:
        if arr[a+1][b] == 1:
          stack.append([a+1, b])
      if b+1 < N and [a, b+1] not in stack:
        if arr[a][b+1] == 1:
          stack.append([a, b+1])
      arr[a][b] = 2
      count += 1
  return arr, count

N = int(input())
#arr = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]
arr = [[0 for i in range(N)] for i in range(N)]
for i in range(N):
  tmp = input()
  arr[i] = [int(x) for x in tmp]

count, count_arr =  solution(arr,N)
print(count)
for x in sorted(count_arr):
  print(x)  