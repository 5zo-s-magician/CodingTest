def solution(lottos, win_nums):
    correct_num1 = 0
    correct_num2 = 0

    for element in lottos:
        for element2 in win_nums:
            if(element == 0):
                correct_num1 += 1
                break
            elif(element == element2):
                correct_num2 += 1
                correct_num1 += 1
                break

    if(correct_num1 > 0):
        correct_num1 = 7-correct_num1
    else:
        correct_num1 = 6

    if(correct_num2 > 0):
        correct_num2 = 7-correct_num2
    else:
        correct_num2 = 6

    answer = [correct_num1, correct_num2]
    return answer
