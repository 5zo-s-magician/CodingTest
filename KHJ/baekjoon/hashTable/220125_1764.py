
def solution(no_listen, no_see):
    set_no_listen = set(no_listen)
    set_no_see = set(no_see)
    answer = list(set_no_listen.intersection(set_no_see))
    answer.sort()
    
    print(len(answer))
    for i in answer:
        print(i)
            

n, m = input().split()
no_listen = []
no_see = []
for i in range(int(n)):
    no_listen.append(input())
for i in range(int(m)):
    no_see.append(input())
solution(no_listen, no_see)
    