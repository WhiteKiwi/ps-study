# 2020-11-28
# 평범한 배낭 12865 https://www.acmicpc.net/problem/12865
import sys
WEIGHT = 0
VALUE = 1

def dp(i, j):
    global DP
    if i <= 0 or j <= 0:
        return 0

    if DP[i][j] == None:
        global objects
        if objects[i - 1][WEIGHT] <= j:
            A = objects[i - 1][VALUE] + dp(i - 1, j - objects[i - 1][WEIGHT])
            B = dp(i - 1, j)
            DP[i][j] = max(A, B)
        else:
            DP[i][j] = dp(i - 1, j)

    return DP[i][j]

[N, T] = list(map(int, sys.stdin.readline().split()))

objects = []
for i in range(N):
    [WEIGHT_i, VALUE_i] = list(map(int, sys.stdin.readline().split()))
    objects.append([WEIGHT_i, VALUE_i])

DP = [[None for x in range(T+1)] for x in range(N+1)]
print(dp(N, T))
