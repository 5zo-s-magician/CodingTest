# 다양한 수로 이루어진 배열 -> 주어진 수들을 M 번 더하여 가장 큰 수를 만드는 법칙
# 단 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.

def solution(M, K, arr):
    arr.sort(reverse = True)
    div, mod = divmod(M, K+1)
    answer = (arr[0]*K)*div + arr[1]*div + arr[0]*mod
    print(answer)

solution(8,3,[2,4,5,4,6])    
    
