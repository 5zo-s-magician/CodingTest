def wine_max(wines, cnt):
    drink = [0] * len(wines)
    drink[1] = wines[1]
    if cnt >= 2:
        drink[2] = wines[1] + wines[2]
    
    for i in range(3, cnt+1):
        drink[i] = max(drink[i-1], drink[i-2]+ wines[i], drink[i-3]+wines[i-1]+wines[i])
    
    return drink[cnt]
    
cnt = int(input())
wines = [0] * (cnt+1)
for i in range(cnt):
    wines[i+1] = int(input())
    
print(wine_max(wines, cnt))