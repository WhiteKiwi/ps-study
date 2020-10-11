# 2020-10-11
# 팰린드롬? 10942 https://www.acmicpc.net/problem/10942
import sys

sys.stdin.readline().split()
arr = list(map(int, sys.stdin.readline().split()))

n = int(sys.stdin.readline())

for i in range(n):
    [a, b] = list(map(int, sys.stdin.readline().split()))
    a -= 1
    arr1 = arr[a:b]
    middle = len(arr1) / 2
    idx = 0
    flag = True
    while idx < middle:
        if arr1[idx] != arr1.pop():
            flag = False
            break
        idx += 1
    if flag:
        print(1)
    else:
        print(0)
