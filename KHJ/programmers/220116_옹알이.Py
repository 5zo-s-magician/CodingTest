def solution(babblings):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]
    
    for babbleing in babblings:
        now = 0
        start = 0
        ok = False
        for now in range(1,len(babbleing)):
            if babbleing[start:now+1] in possible:
                ok = True
                start = now+1
            else:
                ok = False
        if ok:
            answer += 1
            
    return answer