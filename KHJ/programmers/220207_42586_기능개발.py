def solution(progresses, speeds):
    answer = []
    
    # 1. 남은 양 구하기
    left = [100-x for x in progresses]
    
    # 2. 더 필요한 날짜 구하기
    day = [left[i] // speeds[i] +1 if left[i] % speeds[i] != 0 else left[i] // speeds[i] for i in range(len(left)) ]
    
    k = 0
    while k < len(day):
        now = day[k]
        j = k
        while j < len(day) and day[j] <= now :
            j += 1
        count = j - k
        k = j
        answer.append(count)
    return answer





# def solution(progresses, speeds):
#     answer = []
#     days = [dayCal(progresses[i],speeds[i]) for i in range(len(progresses))]
    
#     while len(days) != 0:
#         count = 1
#         first_day = days.pop(0)
#         while len(days) != 0:
#             if days[0] <= first_day:
#                 days.pop(0)
#                 count += 1
#             else:
#                 break
#         answer.append(count)
        
#     return answer

# def dayCal(p,s):
#     day = (100 - p)/s
#     if day%1 != 0:
#         day = int(day)+1
#     return int(day)