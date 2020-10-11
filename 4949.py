# 2020-10-11
# 균형잡힌 세상 4949 https://www.acmicpc.net/submit/4949/23164890
import sys
import re


def check(arr):
    stack = []

    for a in arr:
        if a == '[' or a == '(':
            stack.append(a)
        else:
            if len(stack) == 0:
                return False
            b = stack.pop()

            if a == ')':
                if b != '(':
                    return False
            else:
                if b != '[':
                    return False
    return len(stack) == 0


while True:
    inputs = sys.stdin.readline()
    if inputs == '.\n' or inputs == '.':
        break

    arr = []
    for a in re.findall('[\[\]\(\)]', inputs):
        for s in list(a):
            arr.append(a.strip())
    if check(arr):
        print('yes')
    else:
        print('no')
