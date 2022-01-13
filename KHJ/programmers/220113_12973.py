# 시간 효율성 문제 -> stack을 사용하면 시간 효율성이 높아진다.

#stack을 사용하지 않은 코드
def solution(s):
    idx = 0
    while idx<len(s)-1:
        if s[idx] == s[idx+1]:
            s = s[:idx] + s[idx+2:]
            idx = 0
        else:
            idx += 1
    
    if len(s) == 0:
        return 1
    return 0

# stack을 사용한 코드
def solution(s):
    stack = [s[0]]
    for i in range(1,len(s)):
        try:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        except:
            if i == len(s) -1:
                return 0
            else:
                stack.append(s[i])
    if len(stack) == 0:
         return 1
    else:
        return 0