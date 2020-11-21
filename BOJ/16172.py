# 2020-11-01
# 나는 친구가 적다 (Large) 16172 https://www.acmicpc.net/problem/16172
import sys
import re

originStr = sys.stdin.readline()
targetStr = sys.stdin.readline()
filteredStr = re.sub(r'[0-9]', '', originStr)
if (re.search(targetStr, filteredStr)):
    print(1)
else:
    print(0)
