import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

c = [[0 for i in range(len(str1))] for j in range(len(str2))]

for i in range(len(str2)):
    for j in range(len(str1)):
        if str2[i] == str1[j]:
            if i==0 or j == 0:
                c[i][j] = 1
            else:
                c[i][j] = c[i-1][j-1] + 1
        else:
            if i==0 and j == 0:
                continue
            if i==0:
                c[i][j] = c[i][j-1]
            elif j ==0:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])

end = c[len(str1)-1][len(str2)-1]
print(end)
if end != 0:
    answer = ""
    i = len(str2)-1
    j = len(str1)-1

    while end>0:
        if str1[j] == str2[i]:
            answer = str1[j] + answer
            if i>0:
                i -= 1
            if j>0:
                j -= 1
            end -= 1
        else:
            if c[i][j-1]>= c[i-1][j] and j>0:
                j -= 1
            else:
                i -= 1
                
    print(answer)