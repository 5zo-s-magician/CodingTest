def solution(s):
    index = 0
    tmp = s
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    for i in range(0, len(s)):
        if(s[i].isdigit()):
            answer = str(answer) + str(s[i])
            i += 1
        else:
            for j in range(0, len(word)):
                try:
                    if(s[i:i+len(word[j])] == word[j]):
                        answer = str(answer) + str(j)
                        i += len(word[j])
                        break
                except IndexError:
                    print("hi")
    print(answer)
    # answer = 234
    return int(answer)

solution("2three45sixseven")