def solution(common):
    answer = 0
    btw = [0,0]
    
    for i in range(2):
        btw[i] = common[i+1] - common[i] 
    
    if btw[0] == btw[1]:
        return common[-1] + btw[0]
    
    return common[-1] * (common[1]//common[0])