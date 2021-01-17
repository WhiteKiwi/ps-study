# 2020-01-17
# 아우으 우아으이야!! 15922
import sys

N = int(sys.stdin.readline())

sum = 0
before_y = -1000000000
for _ in range(N):
    [x, y] = list(map(int, sys.stdin.readline().split()))
    if before_y > x:
        if before_y < y:
            sum += y - before_y
            before_y = y
    else:
        sum += y - x
        before_y = y

print(sum)
