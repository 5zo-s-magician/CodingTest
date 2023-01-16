from itertools import permutations

def solution(n, m, x, y, r, c, k):
    se = y-c
    ga = x-r
    left = k - abs(se) - abs(ga)

    if left%2 == 1:
        return "impossible"

    move = []

    if se>0:
        move += ["l" for i in range(se)]
    else:
        move += ["r" for i in range(abs(se))]
    if ga>0:
        move += ["u" for i in range(ga)]
    else:
        move += ["d" for i in range(abs(ga))]
    
    arr = [["d","u"], ["l", "r"]]
    permu_result = permutations(arr, left//2)
    possible_move = []
    for res in permu_result:
        tmp_move = []
        tmp_move += move
        for i in res:
            tmp_move += i
        possible_move.append(tmp_move)
    
    possible_move2 = []
    for i in possible_move:
        possible_move2 += permutations(i, k)
    possible_move2.sort()
    possible_move3 = []
    possible_move2 = [possible_move3.append(xx) for xx in possible_move2 if xx not in possible_move3]
    for move in possible_move3:
        a = x
        b = y
        cnt = 0
        print(move)
    
        for val in move:
            if a<1 or a>n or b<1 or b>m:
                break
            if val == "r":
                b += 1
            if val == "l":
                b -= 1  
            if val == "u":
                a -= 1
            if val == "d":
                a += 1
            cnt += 1
        if cnt == k and not (a<1 or a>n or b<1 or b>m):
            return "".join(move)

    return "".join(move)

print(solution(3, 4, 2, 3, 3, 1, 5))