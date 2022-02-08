from collections import deque

""" int[] nivel = new int[N];
Arrays.fill(nivel, -1);
Queue agenda = new LinkedList<Integer>();
agenda.add(0);
nivel[0] = 0;

while(agenda.size() > 0) {
  int v = agenda.dequeue();
  List<Integer> children = getChildren();

  for(int w: children) {
    if(nivel[w] < 0) {
			nivel[w] = nivel[v] + 1;
			agenda.add(w);    
		}
  }
} """

def BFS(graph: list) -> bool:
  # Creates an empty queue
  # The idea behind this queue is to store non-visited nodes
  visited = []
  queue = []
  visited.append(0)
  queue.append(0)
  nivel: list = [-1 for _ in range(len(graph))]
  # While queue is not empty, will search for paths between all nodes
  while queue:
    current = queue.pop(0)
    for node in graph[current]:
        if nivel[node] < 0 and node not in visited:
            nivel[node] = nivel[current] + 1
            visited.append(node)
            queue.append(node)
    
  # If x > 6 for at least one pair of nodes, it means the theory is false
  print(nivel)
  for x in nivel[1:]:
      if x == -1 or x > 6:
          return False
  return True

# >>> import functools
# >>> functools.reduce(lambda x, y: x or y, (True, False, False))


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

#graph = random_graph(10, 0.2)
#print(graph)
graph = [[1], [0, 4, 5, 8], [5, 9], [8], [1, 5, 8, 9], [1, 2, 4], [], [], [1, 3, 4, 9], [2, 4, 8]]
print(BFS(graph))
