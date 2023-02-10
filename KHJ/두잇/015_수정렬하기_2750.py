import sys
input = sys.stdin.readline

def bubble(arr):
    end = len(arr) - 1
    while end > 0:
        for i in range(end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        end -= 1
    return arr

N = int(input())          
arr = [0]*N

for i in range(N):
    arr[i] = int(input())
    
arr = bubble(arr)

for i in range(N):
    print(arr[i])
            
        