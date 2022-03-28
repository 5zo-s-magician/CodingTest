def solution(N):
    five_hundred, etc = divmod(N,500)
    one_hundred, etc = divmod(etc, 100)
    five_ten, etc = divmod(etc, 50)
    one_ten, etc = divmod(etc,10)
    print(five_hundred)
    print(one_hundred)
    print(five_ten)
    print(one_ten)
    
solution(1260)

# 더 좋은 풀이
def solution2(N):
    coin_types = [500, 100, 50, 10]
    for i in range(4):
        div, N = divmod(N, coin_types[i])
        print(div)

solution2(1260)