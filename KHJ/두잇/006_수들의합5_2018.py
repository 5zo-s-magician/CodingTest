import sys
input = sys.stdin.readline

N = int(input())
answer = 1
sumN = 1
start = 1
end = 1

while end<N:
    if sumN > N:
        sumN -= start
        start += 1
    elif sumN < N:
        end += 1
        sumN += end
    else:
        answer += 1
        end +=1
        sumN += end
        

print(answer)
    