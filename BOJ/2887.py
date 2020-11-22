# 2020-11-21 - map ver - 시간초과
# 행성 터널 2887 https://www.acmicpc.net/problem/2887
import sys
from queue import PriorityQueue

class Node:
    def __init__(self, index, x, y, z):
        self.index = index
        self.x = x
        self.y = y
        self.z = z

x_list = []
y_list = []
z_list = []

def input(node_map, index, x, y, z):
    global x_list
    global y_list
    global z_list
    new_node = Node(index, x, y, z)
    x_list.append({ "val": x, "index": index })
    y_list.append({ "val": y, "index": index })
    z_list.append({ "val": z, "index": index })
    node_map[i] = new_node

def add_edge(edge_map, a, b, dist, pq = None):
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
    if pq != None:
        pq.put((dist, [a, b]))

def make_pq(edge_map, pq):
    for key_a in edge_map.keys():
        for key_b in edge_map[key_a].keys():
            pq.put((edge_map[key_a][key_b], [key_a, key_b]))

def make_edge_map(node_map, edge_map):
    global x_list
    global y_list
    global z_list

    x_list = sorted(x_list, key = lambda x: x["val"])
    for i in range(len(x_list) - 1):
        dist_x = abs(x_list[i]["val"] - x_list[i + 1]["val"])
        add_edge(edge_map, x_list[i]["index"], x_list[i + 1]["index"], dist_x)

    y_list = sorted(y_list, key = lambda x: x["val"])
    for i in range(len(y_list) - 1):
        dist_y = abs(y_list[i]["val"] - y_list[i + 1]["val"])
        add_edge(edge_map, y_list[i]["index"], y_list[i + 1]["index"], dist_y)

    z_list = sorted(z_list, key = lambda x: x["val"])
    for i in range(len(z_list) - 1):
        dist_z = abs(z_list[i]["val"] - z_list[i + 1]["val"])
        add_edge(edge_map, z_list[i]["index"], z_list[i + 1]["index"], dist_z)

def union(node_map, edge_map, a, b, pq):
    for key in edge_map[b.index].keys():
        if key not in node_map:
            continue
        node = node_map[key]
        if node.index != a.index:
            if node.index not in edge_map[a.index]:
                # A랑 node랑 연결이 안되어 있었으면 그냥 추가
                dist_from_b = edge_map[b.index][node.index]
                add_edge(edge_map, a.index, node.index, dist_from_b, pq)
            else:
                dist_from_b = edge_map[b.index][node.index]
                add_edge(edge_map, a.index, node.index, dist_from_b, pq)

    for key in node_map.keys():
        node = node_map[key]
        if node.index != a.index and node.index != b.index and b.index in edge_map and node.index in edge_map[b.index]:
            if node.index not in edge_map[a.index]:
                # A랑 node랑 연결이 안되어 있었으면 그냥 추가
                dist_from_b = edge_map[b.index][node.index]
                add_edge(edge_map, a.index, node.index, dist_from_b, pq)
            else:
                dist_from_b = edge_map[b.index][node.index]
                add_edge(edge_map, a.index, node.index, dist_from_b, pq)

N = int(sys.stdin.readline())
node_map = {}
edge_map = {}
for i in range(N):
    [x, y, z] = list(map(int, sys.stdin.readline().split()))
    input(node_map, i, x, y, z)

make_edge_map(node_map, edge_map)
pq = PriorityQueue()
make_pq(edge_map, pq)

cost = 0
while len(node_map) > 1:
    data = pq.get()
    [a, b] = data[1]
    if a in node_map and b in node_map:
        cost += data[0]
        union(node_map, edge_map, node_map[a], node_map[b], pq)
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
