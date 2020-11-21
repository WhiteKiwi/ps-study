# 2020-10-11
# 트리의 지름 1967 https://www.acmicpc.net/problem/1967
import sys

class Node:
    def __init__(self, dist):
        self.dist = dist
        self.children = []
    
    def input(self, dist):
        new_node = Node(dist)
        self.children.append(new_node)
        return new_node


biggest = 0
def travel(node):
    global biggest
    first = 0
    second = 0
    for i in range(len(node.children)):
        n = travel(node.children[i])
        if second < n:
            if first < n:
                second = first
                first = n
            else:
                second = n
    if biggest < first + second:
        biggest = first + second
    return first + node.dist


n = int(sys.stdin.readline())
root = Node(0)
arr = [None for _ in range(10000)]
arr[0] = root
for i in range(n-1):
    [parent, child, dist] = list(map(int, sys.stdin.readline().split()))
    parent -= 1
    child -= 1
    arr[child] = arr[parent].input(dist)

travel(root)
print(biggest)
