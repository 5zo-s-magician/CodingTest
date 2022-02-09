def solution(a, b):
    answer = 0
    
    
    if a == b:
        answer = a
    elif a > b:
        answer = (a+b)*(a-b+1)/2
    elif a < b:
        answer = (a+b)*(b-a+1)/2
        
    return answer