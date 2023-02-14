#-*- coding:utf-8 -*-
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
finds = list(map(int, input().split()))
arr.sort()


for x in finds:
    start = 0
    end = len(arr) -1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == x:
            print(1)
            break
        elif arr[mid] > x:
            end = mid-1
            continue
        else:
            start = mid+1
    if start>end:
        print(0)
