# 2020-11-22
# 소가 정보섬에 올라온 이유 17128 https://www.acmicpc.net/problem/17128
import sys

[Ncow, Nq] = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))
Q = list(map(int, sys.stdin.readline().split()))

sub = [1 for _ in range(Ncow)]
for i, Ai in enumerate(A):
    for j in range(4):
        # subi = Ai * A(i+1) * A(i+2) * A(i+3)
        sub[i + j if i + j < Ncow else i + j - Ncow] *= Ai

# 최초 1회 S 계산
S = sum(sub)
for Qi in Q:
    Qi -= 1
    # i번째 소가 영향을 준 sub 그룹들의 부호를 바꿔주고 반영
    for j in range(4):
        # 부호 바꾸고
        sub[Qi + j if Qi + j < Ncow else Qi + j - Ncow] *= -1
        # 2배만큼 반대로 반영
        S += sub[Qi + j if Qi + j < Ncow else Qi + j - Ncow] * 2
    print(S)
