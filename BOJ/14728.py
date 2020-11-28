# 2020-11-28
# 벼락치기 14728 https://www.acmicpc.net/problem/14728
import sys
K = 0
S = 1

def dp(i, j):
    global DP
    if i <= 0 or j <= 0:
        return 0

    if DP[i][j] == None:
        global subjects
        if subjects[i - 1][K] <= j:
            A = subjects[i - 1][S] + dp(i - 1, j - subjects[i - 1][K])
            B = dp(i - 1, j)
            DP[i][j] = max(A, B)
        else:
            DP[i][j] = dp(i - 1, j)

    return DP[i][j]

[N, T] = list(map(int, sys.stdin.readline().split()))

subjects = []
for i in range(N):
    [Ki, Si] = list(map(int, sys.stdin.readline().split()))
    subjects.append([Ki, Si])

DP = [[None for x in range(T+1)] for x in range(N+1)]
print(dp(N, T))
