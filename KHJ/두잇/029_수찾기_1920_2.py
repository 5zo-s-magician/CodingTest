import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().split()))

M = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for x in arr2:
    s = 0
    e = len(arr1) -1
    good = False
    while s <= e:
        m = (s+e)//2
        if arr1[m] == x:
            print(1)
            good = True
            break
        elif arr1[m] > x:
            e = m - 1
        else:
            s = m + 1
    if not good:
        print(0)



# 타임아웃 아마 N*M이라서 그럴듯
# for x in arr2:
#     if x in arr1:
#         print(1)
#     else:
#         print(0)