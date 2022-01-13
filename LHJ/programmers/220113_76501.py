def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(absolutes)):
        value = absolutes[i]
        if(signs[i] == False):
            value = value*(-1)
        answer += value
        
    return answer