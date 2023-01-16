# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(stack1, stack2, stack3):
    # write your code in Python 3.8.10
    arr  = []
    for x in stack1:
        arr.append([1,x])
    for x in stack2:
        arr.append([2,x])
    for x in stack3:
        arr.append([3,x])
    
    arr.sort(key=lambda x: x[1], reverse=True)
    answer_turn = [str(arr[x][0]) for x in range(len(arr))]

    return "".join(answer_turn)