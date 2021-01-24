# 2021-01-24
# 폰트 9997 https://www.acmicpc.net/problem/9997
import sys


def char_to_bit(char):
    # a -> 1, z -> 10000 00000 00000 00000 00000 0
    return 1 << (ord(char) - 97)


def travel(index, sentence):
    global N
    if sentence == 0b11111111111111111111111111:
        return 2 ** (N - index)
    if index == N:
        return 0

    global words
    # 이번 문자를 포함한 경우와 포함하지 않은 경우
    return travel(index + 1, sentence) + travel(index + 1, sentence | words[index])


N = int(sys.stdin.readline())

words = []
for _ in range(N):
    word = 0
    for char in sys.stdin.readline().strip():
        word |= char_to_bit(char)
    words.append(word)

count_of_case = travel(0, 0)
print(count_of_case)
