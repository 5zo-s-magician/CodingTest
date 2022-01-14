def solution(n, words):
    who = -7
    for idx,word in enumerate(words):
        if idx == 0:
            continue
        if word in words[:idx] or (word[0] != words[idx-1][-1]):
            #print(word, words[:idx])
            #print(word[0], words[idx-1][-1])
            
            # 7번째 - 3 2,1 (1번쨰 사람, 3번쨰 턴)
            turn, who = divmod(idx+1, n)
            if who == 0:
                who = n
            else:
                turn += 1
            break

    if who == -7:
        return [0,0]
    
    return [who, turn]