def solution(array, commands):
    answer = []
    
    for i in range(0, len(commands)):
        tmparr = array[commands[i][0]-1:commands[i][1]]
        tmparr.sort()
        answer.append(tmparr[commands[i][2]-1])
        
    return answer