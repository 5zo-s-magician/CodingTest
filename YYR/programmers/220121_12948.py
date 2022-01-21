def solution(phone_number):
    answer = ''
    last1 = phone_number[::-1]
    print(last1)
    last2 = last1[:4]
    print(last2)
    for i in range(len(phone_number)-4):
        answer += '*'
    answer += last2[::-1]
    
    return answer