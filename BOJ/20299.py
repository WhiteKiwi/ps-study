# 2020-12-20
# 3대 측정 20299 https://www.acmicpc.net/problem/20299
import sys

[N, K, L] = list(map(int, sys.stdin.readline().split()))

result = []
for i in range(N):
    team = list(map(int, sys.stdin.readline().split()))
    if sum(team) < K:
        continue
    if min(team) < L:
        continue
    result.append(team)

print(len(result))
for team in result:
    for rating in team:
        print(rating, end=' ')
