def solution(num, total):
    div,mod = divmod(num,2)
    base = 0
    
    if mod != 0:    #홀수
        base = (total // num)  - (num-1)//2
    else:
        base = ((total - num//2) // num) - (num//2-1)
    
    answer = [base + i for i in range(num)]
    
    return answer