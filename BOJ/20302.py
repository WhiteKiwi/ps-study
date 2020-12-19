# 2020-12-20
# 민트 초코 20302 https://www.acmicpc.net/problem/20302
import sys
import re

def split_one(text):
    return int(text[1])

# 첫 줄 버리고
sys.stdin.readline()
# 두 번째 줄 받아서
text = sys.stdin.readline()
# 공백 지우고
text = text.replace(' ', '')

# 앞에 * 붙은 친구들 가져오기
multiplies = list(map(split_one, re.findall(r'\*[0-9]', text)))
# 맨 앞 친구 곱하는 친구들에 추가
multiplies.append(int(text[0]))
# 앞에 / 붙은 친구들 가져오기
divides = list(map(split_one, re.findall(r'\/[0-9]', text)))

# 합산해서 계산
result = 1
for multiply_num in multiplies:
    result *= multiply_num
for divide_num in divides:
    result /= divide_num

if result.is_integer():
    print('mint chocolate')
else:
    print('toothpaste')
