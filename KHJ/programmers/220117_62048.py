def solution(w,h):
    #최소공약수
    p,q = w,h
    while q != 0:
        p,q = q, p % q
    gcd = p
    
    ws = w//gcd
    hs = h//gcd
    
    return w*h - ((ws+hs-1)*gcd)