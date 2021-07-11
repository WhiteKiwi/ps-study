# 2021-07-11
# Router 15828 https://www.acmicpc.net/problem/15828
import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()
while(True):
    packet = sys.stdin.readline()
    if (packet == '0\n'):
        queue.popleft()
        continue
    if (packet == '-1\n'):
        break
    if (len(queue) < N):
        queue.append(packet.rstrip())

if (len(queue) == 0):
    print('empty')
else:
    print(' '.join(list(queue)))
