# 2020-11-21
# 행성 터널 2887 https://www.acmicpc.net/problem/2887
import sys

class Node:
    def __init__(self, index, x, y, z):
        self.index = index
        self.x = x
        self.y = y
        self.z = z
        self.is_removed = False

def input(node_list, edge_map, index, x, y, z):
    new_node = Node(index, x, y, z)
    for node in node_list:
        dist = min([abs(node.x - x), abs(node.y - y), abs(node.z - z)])
        edge_map[f'{index}-{node.index}'] = dist
        edge_map[f'{node.index}-{index}'] = dist
    node_list.append(new_node)

def union(node_list, edge_map, a, b):
    for node in node_list:
        if node.is_removed:
            continue
        if node.index != a.index and node.index != b.index:
            dist_from_a = edge_map[f'{a.index}-{node.index}']
            dist_from_b = edge_map[f'{b.index}-{node.index}']
            # a와의 거리를 a, b 중 짧은 것으로 통일하고
            if dist_from_a > dist_from_b:
                edge_map[f'{a.index}-{node.index}'] = dist_from_b
                edge_map[f'{node.index}-{a.index}'] = dist_from_b
            # b를 지움
            del edge_map[f'{b.index}-{node.index}']
            del edge_map[f'{node.index}-{b.index}']
    del edge_map[f'{a.index}-{b.index}']
    del edge_map[f'{b.index}-{a.index}']

N = int(sys.stdin.readline())
node_list = []
edge_map = {}
for i in range(N):
    [x, y, z] = list(map(int, sys.stdin.readline().split()))
    input(node_list, edge_map, i, x, y, z)

cost = 0
while len(edge_map) != 0:
    closest_edge = min(edge_map, key=edge_map.get)
    [a, b] = list(map(int, closest_edge.split('-')))
    cost += edge_map[closest_edge]
    union(node_list, edge_map, node_list[a], node_list[b])
    node_list[b].is_removed = True

print(cost)

# # 2020-11-21
# # 행성 터널 2887 https://www.acmicpc.net/problem/2887
# import sys

# class Node:
#     def __init__(self, index, x, y, z):
#         self.index = index
#         self.x = x
#         self.y = y
#         self.z = z
#         self.is_removed = False

# def input(node_list, edge_map, index, x, y, z):
#     new_node = Node(index, x, y, z)
#     for node in node_list:
#         dist = min([abs(node.x - x), abs(node.y - y), abs(node.z - z)])
#         edge_map[index][node.index] = dist
#         edge_map[node.index][index] = dist
#     node_list.append(new_node)

# def union(node_list, edge_map, a, b):
#     for node in node_list:
#         if node.is_removed:
#             continue
#         if node.index != a.index and node.index != b.index:
#             dist_from_a = edge_map[a.index][node.index]
#             dist_from_b = edge_map[b.index][node.index]
#             # a와의 거리를 a, b 중 짧은 것으로 통일하고
#             if dist_from_a > dist_from_b:
#                 edge_map[a.index][node.index] = dist_from_b
#                 edge_map[node.index][a.index] = dist_from_b
#             # b와 node의 거리를 최대로 설정
#             edge_map[b.index][node.index] = sys.maxsize
#             edge_map[node.index][b.index] = sys.maxsize
#         edge_map[b.index][a.index] = sys.maxsize
#         edge_map[a.index][b.index] = sys.maxsize

# N = int(sys.stdin.readline())
# node_list = []
# edge_map = [[sys.maxsize for _ in range(N)] for _ in range(N)]
# for i in range(N):
#     [x, y, z] = list(map(int, sys.stdin.readline().split()))
#     input(node_list, edge_map, i, x, y, z)

# cost = 0
# for i in range(N-1):
#     min_arr = min(edge_map)
#     min_dist = min(min_arr)
#     a = edge_map.index(min_arr)
#     b = min_arr.index(min_dist)
#     cost += min_dist
#     union(node_list, edge_map, node_list[a], node_list[b])
#     node_list[b].is_removed = True

# print(cost)
