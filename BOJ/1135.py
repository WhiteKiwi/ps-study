# 2020-05-02
# 뉴스 전하기 1135 https://www.acmicpc.net/problem/1135
import sys

class Node:
    def __init__(self, depth):
        self.depth = depth
        self.children = []
        self.time = 0

def travel(node):
    # child의 최대 시간으로 정렬
    for child in node.children:
        child.time = travel(child)
    node.children.sort(key = lambda x: x.time, reverse=True)
    
    max_time = 0
    for i, child in enumerate(node.children):
        # i + 1(현재 노드에 요청 보내기까지 걸린 시간) + child.time
        # 요청을 받은 순간부터 요청을 시작하므로 (노드가 수행되는데 필요한 시간 + 요청 순서)의 최댓값이 최소로 필요한 시간이라고 할 수 있음
        if i + 1 + child.time > max_time:
            max_time = i + 1 + child.time

    return max_time

node_list = []
# N = int(sys.stdin.readline())
sys.stdin.readline()
parent_indices = list(map(int, sys.stdin.readline().split()))

# 트리 생성
for parent_index in parent_indices:
    if parent_index == -1:
        node = Node(0)
        node_list.append(node)
        continue

    parent_node = node_list[parent_index]

    # 부모 depth + 1로 child 생성
    node = Node(parent_node.depth + 1)
    node_list.append(node)
    parent_node.children.append(node)

max_time = travel(node_list[0])

print(max_time)
