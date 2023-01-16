import math

def solution(numbers):
    answer = []
    # 1. 높이와 노드 개수가 가능한지 확인하기 -> 포화 이진트리 h -> 노드개수: 2^h-1
    for idx, number in enumerate(numbers):
        binary_num = bin(number)[2:]
        if math.log2(len(binary_num))%1.0 != 0:
            answer.append(0)
            continue
        answer.append(1)
    
    return answer

numbers = [63, 111, 95]
solution(numbers)