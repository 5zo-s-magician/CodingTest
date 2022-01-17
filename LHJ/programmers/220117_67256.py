def solution(numbers, hand):
    # position = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [11, 0, 12]]
    position = [[3, 1]]
    l_position = [3, 0]
    r_position = [3, 2]
    answer = ''
    
    for i in range(0, 9):
        position.append([int(i/3), i%3])
    # print(position)
    
    for i in numbers:
        l_distance = abs(position[i][0] - l_position[0]) + abs(position[i][1] - l_position[1])
        r_distance = abs(position[i][0] - r_position[0]) + abs(position[i][1] - r_position[1])
        # print(str(l_distance) + ' | ' +str(r_distance) )
        if(i in [3, 6, 9]):
            answer = answer + 'R'
            r_position = [position[i][0], position[i][1]]
        elif(i in [1, 4, 7]):
            answer = answer + 'L'
            l_position = [position[i][0], position[i][1]]
        else:
            if(l_distance > r_distance):
                answer = answer + 'R'
                r_position = [position[i][0], position[i][1]]
            elif(l_distance < r_distance):
                answer = answer + 'L'
                l_position = [position[i][0], position[i][1]]
            else:
                if(hand == "right"):
                    answer = answer + 'R'
                    r_position = [position[i][0], position[i][1]]
                else:
                    answer = answer + 'L'
                    l_position = [position[i][0], position[i][1]]
                
    return answer