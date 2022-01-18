N, L, W, H = map(int, input().split())
b = 0
e = min(L, W, H)

for i in range(10000):
    mid = (b + e) / 2
    if (L//mid)*(W//mid)*(H//mid) < N:
        e = mid
    else:b = mid

print(b)
