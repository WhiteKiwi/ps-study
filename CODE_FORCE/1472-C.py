# 2020-01-24
# C. Long Jumps 1472 https://codeforces.com/problemset/problem/1472/C
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    # This is the same code as `dp = [0 for _ in range(n)]`
    dp = [0] * n
    a_max = 0
    for i in range(n):
        # This is the same code as `for i in reversed(range(n)):`
        i = n - i - 1

        dp[i] = A[i]
        if A[i] + i < n:
            dp[i] += dp[A[i] + i]

        if dp[i] > a_max:
            a_max = dp[i]
    print(a_max)
