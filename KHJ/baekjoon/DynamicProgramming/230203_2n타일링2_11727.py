def tile(N):
    f = [0] * (N+1)
    f[1] = 1
    if(N>=2):
        f[2] = 3
    
    for i in range(3, N+1):
        f[i] = f[i-1] + f[i-2]*2
        
    return f[N]

N = int(input())

print(tile(N)%10007)
    