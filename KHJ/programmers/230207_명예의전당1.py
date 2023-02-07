from heapq import heappush, heappop

def solution(k, score):
    myeoung_ye = []
    answer = []
    for x in score:
        heappush(myeoung_ye, x)
        if(len(myeoung_ye)>k):
            heappop(myeoung_ye)
        answer.append(myeoung_ye[0])
    return answer