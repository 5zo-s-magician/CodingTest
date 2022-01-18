def min_val(a, b, c):
    if(a < b):
        if(a < c):
            return a
        else:
            return c
    else:
        if(b < c):
            return b
        else:
            return c

def present(n, l, w, h):
    answer = 0
    prev_answer = 1
    min = 0
    max = min_val(l, w, h) # 적어도 한 개의 정육면체 박스가 들어갈 수 있는 값
    #이제 이진탐색을 하면서 int(l/answer)*int(w/answer)*int(h/answer) >= n을 만족시키는
    #최대 answer값을 찾아낸다. 즉 저 값이 n-1이 되는 순간의 값..

    while(int(prev_answer*(10**30)) != int(answer*(10**30))):
        # print("======")
        # print(prev_answer)
        # print(answer)
        answer = (min+max)/2
        enable_box_num = int(l/answer)*int(w/answer)*int(h/answer)
        if(enable_box_num >= n): # answer을 더 키울 수 있단 소리
            min = answer
            prev_answer = answer
            answer = (min+max)/2
            #해서 다시 검사
        else:
            max = answer
            prev_answer = answer
            answer = (min+max)/2

    return answer


a, b, c, d = input().split()
result = present(int(a), int(b), int(c), int(d))
print(result)

    