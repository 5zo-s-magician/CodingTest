# 작은 거의 크기가 큰거의 크기의 90%보다도 작을때 -> 검사 x

def solution(n, array):
    array.sort()
    for i in range(len(array)):
        value = array[i]*1.9 // 1
        mid = len(array) //2
        start = i+1
        end = len(array) - 1
        
        # value와 같거나 작은 부분 찾아야 함.
        while start<=end:
            mid = (start + end) // 2
            if value > array[mid]:
                start = mid
            elif value == array[mid]:
                while value == array[mid]:
                    mid += 1
                mid -=1
                break
            else:
                end = mid
                
        
        


_input_ = input().split()
print(solution(_input_[0], _input_[1:]))

