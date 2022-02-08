from collections import deque


def BFS(graph, start, end):
    queue = deque()
    queue.append([start])
    while queue:
        path = list(queue.popleft())
        last =  path[-1]
        if last == end:
            print(f"Ruta {path}")
            if len(path) <= 6:
                print("Ruta de 6 o menos")
                print(f"Ruta {path}")
        for node in graph[last]:
            if node not in path:
                new_path = list()
                new_path = path + [node]
                queue.append(new_path)


from random import random
from itertools import product, combinations

def random_graph(n, p, *, directed=False):
    nodes = range(n)
    adj_list = [[] for i in nodes]
    possible_edges = product(nodes, repeat=2) if directed else combinations(nodes, 2)
    for u, v in possible_edges:
        if random() < p:
            adj_list[u].append(v)
            if not directed:
                adj_list[v].append(u)
    for i, el in enumerate(adj_list):
        print(f"{i} esta conectado con -> {el}")
    return adj_list

graph = random_graph(10, 0.5)

BFS(graph, 0, 9)
