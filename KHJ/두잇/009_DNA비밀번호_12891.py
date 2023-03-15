import sys
input = sys.stdin.readline

S, P = map(int, input().split())
string = input().rstrip()
A, C, G, T = map(int, input().split())
alpha = {"A":0, "C":0, "G":0, "T":0}
start = 0
end = start + P - 1
answer = 0

for x in string[start:end]:
    alpha[x] += 1

while end < S:
    alpha[string[end]] += 1
    if alpha["A"] >= A and alpha["C"] >= C and alpha["G"] >= G and alpha["T"] >= T:
        answer += 1
    alpha[string[start]] -= 1
    start += 1
    end += 1
    
    
print(answer)