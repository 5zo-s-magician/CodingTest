def solution(n):
    answer = ""
    arr = ["1","2","4"]
    n = n-1
    while n>=0:
        div,mod = divmod(n,3)
        answer = arr[mod] + answer
        n = div
        n -= 1
    return answer