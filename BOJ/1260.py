# 2020-12-12
# DFS와 BFS 1260 https://www.acmicpc.net/problem/1260
import sys

class Node:
    def __init__(self, index):
        self.index = index
        self.is_visited = False
        self.link = []

def DFS(v, node_list):
    current_node = node_list[v]
    
    current_node.is_visited = True
    print(v + 1, end=' ')

    for link in current_node.link:
        if not node_list[link].is_visited:
            DFS(link, node_list)

def BFS(start, node_list):
    q = []
    q.append(start)
    node_list[start].is_visited = True

    while len(q) > 0:
        current = q.pop(0)
        print(current + 1, end=' ')

        for link in node_list[current].link:
            if not node_list[link].is_visited:
                node_list[link].is_visited = True
                q.append(link)

[N, M, V] = list(map(int, sys.stdin.readline().split()))

node_list = []

for i in range(N):
    node = Node(i)
    node_list.append(node)

for i in range(M):
    [edge_1, edge_2] = list(map(int, sys.stdin.readline().split()))
    node_list[edge_1 - 1].link.append(edge_2 - 1)
    node_list[edge_2 - 1].link.append(edge_1 - 1)

for i in range(N):
    node_list[i].link.sort()
DFS(V - 1, node_list)
print()
for i in range(N):
    node_list[i].is_visited = False
BFS(V - 1, node_list)
