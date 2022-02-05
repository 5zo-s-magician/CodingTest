def solution(numbers):
    answer = []
    
    for i in range(0, len(numbers)):
        try:
            for j in range(i+1, len(numbers)):
                answer.append(numbers[i]+numbers[j])
        except:
            pass
    answer = sorted(set(answer))
    answer = list(answer)
    
    return answer