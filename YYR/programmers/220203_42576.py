def solution(participant, completion):
    answer = ''
    

    hash = {}
    for i in participant:
        if hash.get(i):
            hash[i] += 1 #해쉬테이블을 검색해서 key 값이 있으면 +1 을 해줌 (동명이인 처리)
        else:
            hash[i] = 1 #모든 참여자 리스트를 해시테이블에 저장 

    for i in completion: 
        hash[i] -= 1 #완주한 사람들은 원래 리스트에서 value값 모두 수정
            
    for i in hash:
        if hash[i] > 0:
            answer = i
    
            
    return answer