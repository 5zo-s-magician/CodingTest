def solution(arr):
    min_arr = [min(arr[i]) for i in range(len(arr))]
    answer = max(min_arr)
    print(answer)

arr = [[3,1,2],[4,1,4],[2,2,2]]
arr1 = [[7,3,1,8],[3,3,3,4]]
solution(arr1)
    