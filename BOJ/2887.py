# 2020-11-21 - map ver - 시간초과
# 행성 터널 2887 https://www.acmicpc.net/problem/2887
import sys

class Node:
    def __init__(self, index, x, y, z):
        self.index = index
        self.x = x
        self.y = y
        self.z = z

def input(node_map, index, x, y, z):
    new_node = Node(index, x, y, z)
    node_map[i] = new_node

def find_min(node_map, val, index_to_exclude, get_dist):
    minimum_node = None
    min_dist = sys.maxsize
    for key in node_map.keys():
        dist = get_dist(node_map[key], val)
        if node_map[key].index != index_to_exclude and min_dist > dist:
            min_dist = dist
            minimum_node = node_map[key]
    return minimum_node

def get_dist_x(node, val):
    return abs(node.x - val)

def get_dist_y(node, val):
    return abs(node.y - val)

def get_dist_z(node, val):
    return abs(node.z - val)

def add_edge(edge_map, a, b, arr):
    dist = min(arr)
    if a in edge_map:
        if b not in edge_map[a] or dist < edge_map[a][b]:
            edge_map[a][b] = dist
    else:
        edge_map[a] = { b: dist }
    if b in edge_map:
        if a not in edge_map[b] or dist < edge_map[b][a]:
            edge_map[b][a] = dist
    else:
        edge_map[b] = { a: dist }

def make_edge_map(node_map, edge_map):
    for key in node_map.keys():
        node = node_map[key]
        closest_node_x = find_min(node_map, node.x, node.index, get_dist_x)
        closest_node_y = find_min(node_map, node.y, node.index, get_dist_y)
        closest_node_z = find_min(node_map, node.z, node.index, get_dist_z)
        dist_x = abs(closest_node_x.x - node.x)
        dist_y = abs(closest_node_y.y - node.y)
        dist_z = abs(closest_node_z.z - node.z)
        if closest_node_x.index == closest_node_y.index:
            if closest_node_x.index == closest_node_z.index: # x=y=z
                add_edge(edge_map, closest_node_x.index, node.index, [dist_x, dist_y, dist_z])
            else: # x=y!=z
                add_edge(edge_map, closest_node_x.index, node.index, [dist_x, dist_y])
                add_edge(edge_map, closest_node_z.index, node.index, [dist_z])
        elif closest_node_x.index == closest_node_z.index: # x=z!=y
            add_edge(edge_map, closest_node_x.index, node.index, [dist_x, dist_z])
            add_edge(edge_map, closest_node_y.index, node.index, [dist_y])
        elif closest_node_y.index == closest_node_z.index: # x!=y=z
            add_edge(edge_map, closest_node_y.index, node.index, [dist_y, dist_z])
            add_edge(edge_map, closest_node_x.index, node.index, [dist_x])
        else: # x!=y!=z
            add_edge(edge_map, closest_node_x.index, node.index, [dist_x])
            add_edge(edge_map, closest_node_y.index, node.index, [dist_y])
            add_edge(edge_map, closest_node_z.index, node.index, [dist_z])

def union(node_map, edge_map, a, b):
    for key in node_map.keys():
        node = node_map[key]
        if node.index != a.index and node.index != b.index and b.index in edge_map and node.index in edge_map[b.index]:
            if node.index not in edge_map[a.index]:
                # A랑 node랑 연결이 안되어 있었으면 그냥 추가
                dist_from_b = edge_map[b.index][node.index]
                add_edge(edge_map, a.index, node.index, [dist_from_b])
            else:
                dist_from_a = edge_map[a.index][node.index]
                dist_from_b = edge_map[b.index][node.index]
                # a와의 거리를 a, b 중 짧은 것으로 통일하고
                if dist_from_a > dist_from_b:
                    add_edge(edge_map, a.index, node.index, [dist_from_b])
            # b와 연결된 간선 제거
            del edge_map[b.index][node.index]
            del edge_map[node.index][b.index]
    del edge_map[b.index][a.index]
    del edge_map[a.index][b.index]

def get_min_edge(edge_map):
    min_a = None
    min_b = None
    min_dist = sys.maxsize
    for key_a in edge_map.keys():
        for key_b in edge_map[key_a]:
            if edge_map[key_a][key_b] < min_dist:
                min_dist = edge_map[key_a][key_b]
                min_a = key_a
                min_b = key_b
    return [min_a, min_b, min_dist]

N = int(sys.stdin.readline())
node_map = {}
edge_map = {}
for i in range(N):
    [x, y, z] = list(map(int, sys.stdin.readline().split()))
    input(node_map, i, x, y, z)

make_edge_map(node_map, edge_map)

cost = 0
for i in range(N-1):
    [a, b, min_dist] = get_min_edge(edge_map)
    cost += min_dist
    union(node_map, edge_map, node_map[a], node_map[b])
    del node_map[b]

print(cost)

# # 2020-11-21 - map ver - 메모리 초과
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
#         edge_map[f'{index}-{node.index}'] = dist
#         edge_map[f'{node.index}-{index}'] = dist
#     node_list.append(new_node)

# def union(node_list, edge_map, a, b):
#     for node in node_list:
#         if node.is_removed:
#             continue
#         if node.index != a.index and node.index != b.index:
#             dist_from_a = edge_map[f'{a.index}-{node.index}']
#             dist_from_b = edge_map[f'{b.index}-{node.index}']
#             # a와의 거리를 a, b 중 짧은 것으로 통일하고
#             if dist_from_a > dist_from_b:
#                 edge_map[f'{a.index}-{node.index}'] = dist_from_b
#                 edge_map[f'{node.index}-{a.index}'] = dist_from_b
#             # b를 지움
#             del edge_map[f'{b.index}-{node.index}']
#             del edge_map[f'{node.index}-{b.index}']
#     del edge_map[f'{a.index}-{b.index}']
#     del edge_map[f'{b.index}-{a.index}']

# N = int(sys.stdin.readline())
# node_list = []
# edge_map = {}
# for i in range(N):
#     [x, y, z] = list(map(int, sys.stdin.readline().split()))
#     input(node_list, edge_map, i, x, y, z)

# cost = 0
# while len(edge_map) != 0:
#     closest_edge = min(edge_map, key=edge_map.get)
#     [a, b] = list(map(int, closest_edge.split('-')))
#     cost += edge_map[closest_edge]
#     union(node_list, edge_map, node_list[a], node_list[b])
#     node_list[b].is_removed = True

# print(cost)


# # 2020-11-21 - arr ver - 메모리 초과
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
