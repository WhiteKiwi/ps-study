# 2020-10-18
# 별 찍기 - 10 2447 https://www.acmicpc.net/problem/2447
import sys

MAX = 2187
matrix = [[False for col in range(MAX)] for row in range(MAX)]

def draw(x, y, n):
    global matrix
    a = n // 3

    if n == 1:
        matrix[x][y] = True
        return
    draw(x, y, a)
    draw(x + a, y, a)
    draw(x + 2 * a, y, a)
    draw(x, y + a, a)
    # 중간은 출력 X - draw(x + a, y + a, a)
    draw(x + 2 * a, y + a, a)
    draw(x, y + 2 * a, a)
    draw(x + a, y + 2 * a, a)
    draw(x + 2 * a, y + 2 * a, a)


n = int(sys.stdin.readline())

draw(0, 0, n)

for x in range(n):
    for y in range(n):
        if matrix[x][y]:
            print('*', end='')
        else:
            print(' ', end='')
    print()

"""
# 위의 풀이는 *을 표시하는 거였다면 아래의 풀이는 ' '(공백)을 표시하는 풀이
import sys

MAX = 2187
matrix = [[True for col in range(MAX)] for row in range(MAX)]

def draw(x, y, n, is_middle = False):
    global matrix
    a = n // 3

    if n == 1:
        if is_middle:
            matrix[x][y] = False
        return
    draw(x, y, a, is_middle)
    draw(x + a, y, a, is_middle)
    draw(x + 2 * a, y, a, is_middle)
    draw(x, y + a, a, is_middle)
    draw(x + a, y + a, a, True)
    draw(x + 2 * a, y + a, a, is_middle)
    draw(x, y + 2 * a, a, is_middle)
    draw(x + a, y + 2 * a, a, is_middle)
    draw(x + 2 * a, y + 2 * a, a, is_middle)


n = int(sys.stdin.readline())

draw(0, 0, n)

for x in range(n):
    for y in range(n):
        if matrix[x][y]:
            print('*', end='')
        else:
            print(' ', end='')
    print()
"""
