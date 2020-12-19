# 2020-12-20
# 최소 힙 1927 https://www.acmicpc.net/problem/1927
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
            print(q.get())
    else:
        q.put(n)
