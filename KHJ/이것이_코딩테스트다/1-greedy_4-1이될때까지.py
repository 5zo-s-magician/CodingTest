def solution(N,K):
    count = 0
    while N>1:
        if N%K == 0:
            N //= K
            count +=1
        else:
            N -= 1
            count += 1
    print(count)

solution(25, 5)

def solution1(N,K):
    count = 0
    while N>1:
        N, mod = divmod(N,K)
        count += mod
        count += 1
    print(count)

solution1(17, 4)