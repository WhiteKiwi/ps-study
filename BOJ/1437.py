# 2020-01-17
# 수 분해 1437
import sys
import math

N = int(sys.stdin.readline())

k = 1
while N > 4:
    k *= 3
    k %= 10007
    N -= 3
k *= N
k %= 10007

print(k)
