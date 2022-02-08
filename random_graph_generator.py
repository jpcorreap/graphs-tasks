
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

random = random_graph(10, 0.25)
print(random)