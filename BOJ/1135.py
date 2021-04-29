# 2020-05-02
# 뉴스 전하기 1135 https://www.acmicpc.net/problem/1135
import sys

class Node:
    def __init__(self, depth):
        self.depth = depth
        self.children = []
        self.children_length = 0
        self.time = 0

def travel(node):
    # child의 최대 시간으로 정렬
    for child in node.children:
        child.time = travel(child)
    node.children.sort(key = lambda x: x.time, reverse=True)
    
    max_time_of_node = 0
    for i, child in enumerate(node.children):
        # 1(현재 노드에 요청 보내는 시간) + child.time + index의 최댓값이 이 노드의 최소 시간
        # 요청을 돌리면 그 노드도 요청을 시작하므로 (자식이 필요한 시간 + 정렬 후 순서)의 최댓값이 최소 시간이라고 할 수 있음
        if i + child.time + 1 > max_time_of_node:
            max_time_of_node = i + child.time + 1

    return max_time_of_node

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
    # 부모 children_length ++
    parent_node.children_length += 1

    # 부모 depth + 1로 child 생성
    node = Node(parent_node.depth + 1)
    parent_node.children.append(node)
    node_list.append(node)

max_time = travel(node_list[0])

print(max_time)
