# 2020-10-11
# 트리의 지름 1967 https://www.acmicpc.net/problem/1967
import sys

class Node:
    def __init__(self, index, dist):
        self.index = index
        self.dist = dist
        self.value = None
        if index != 0:
            self.left = Node(0, 0)
            self.right = Node(0, 0)
    
    def get_value(self):
        if self.index == 0:
            return 0
        if self.value != None:
            return self.value
        
        if self.dist < self.left.get_value() and self.dist < self.right.get_value():
            return self.left.get_value() + self.right.get_value()
        elif self.left.get_value() < self.dist and self.left.get_value() < self.right.get_value():
            return self.dist + self.right.get_value()
        else:
            return self.left.get_value() + self.dist
    
    def input(self, index, dist):
        if self.left.index == 0:
            self.left = Node(index, dist)
            return self.left
        else:
            self.right = Node(index, dist)
            return self.right


biggest = 0
def travel(node, sub_dist):
    global biggest
    if node.index == 0:
        return 0
    left = travel(node.left, 0)
    right = 0
    if node.dist + sub_dist < left:
        right = travel(node.right, left)
    else:
        right = travel(node.right, node.dist + sub_dist)
    
    node.value = left + right
    if biggest < node.value:
        biggest = node.value
    
    if left <= right and left <= node.dist + sub_dist:
        return right + node.dist
    elif right <= left and right <= node.dist + sub_dist:
        return left + node.dist
    else:
        if left > right:
            return node.dist + left
        return node.dist + right


n = int(sys.stdin.readline())
root = Node('1', 0)
arr = []
arr.append(root)
for i in range(n-1):
    [parent, child, dist] = list(map(int, sys.stdin.readline().split()))
    parent -= 1
    child -= 1
    child_node = arr[parent].input(i + 2, dist)
    arr.append(child_node)

travel(root, 0)
print(biggest)

# 입력 잘 들어갔는지 확인
# for i in range(n-1):
#    print(arr[i].index, arr[i].left.index, arr[i].right.index, arr[i].dist)
