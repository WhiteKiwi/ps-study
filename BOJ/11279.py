# 2020-12-20
# 최대 힙 11279 https://www.acmicpc.net/problem/11279
import sys
from queue import PriorityQueue

q = PriorityQueue()

N = int(sys.stdin.readline())

for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        if q.qsize() == 0:
            print(0)
        else:
            print(q.get()[1])
    else:
        q.put((sys.maxsize - n, n))
