# 2020-12-20
# 절댓값 힙 11286 https://www.acmicpc.net/problem/11286
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
        q.put((abs(n), n))
