# 2020-10-25
# 집합 11723 https://www.acmicpc.net/problem/11723
import sys

M = int(sys.stdin.readline())

S = 0
for i in range(M):
    calculation = sys.stdin.readline().split()
    if calculation[0] == 'check':
        n = 2 ** (int(calculation[1]) - 1)
        if S & n == n:
            print(1)
        else:
            print(0)
    elif calculation[0] == 'add':
        n = 2 ** (int(calculation[1]) - 1)
        S = S | n
    elif calculation[0] == 'remove':
        n = 2 ** (int(calculation[1]) - 1)
        S = S & (2097151 ^ n)
    elif calculation[0] == 'toggle':
        n = 2 ** (int(calculation[1]) - 1)
        S = S ^ n 
    elif calculation[0] == 'all':
        S = 2097151
    elif calculation[0] == 'empty':
        S = 0
