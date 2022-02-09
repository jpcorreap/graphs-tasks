# 1. La teoría de los seis grados de separación dice que una persona podría conocer a cualquier
# otra persona del mundo siguiendo una cadena de personas que se conocen entre si de tamaño
# máximo 6. Suponiendo que si una persona conoce a otra, entonces tienen una relación de
# amistad en la red social Facebook, diseñar un algoritmo lo más eficiente posible, que reciba la
# base de datos de relaciones de amistad de esta red social y determine si la teoria de los seis
# grados de separación se cumple

from collections import deque

def bfs_with_level(graph):
    # Create array for keeping visited vertex
    visited = [False for _ in range(len(graph))]
    # Queue for proccesing all vertex
    queue = deque()
    # Start with first vertex
    queue.append(0)
    # Mark as visited first vertex
    visited[0] = True
    # Keep in track the number of edges separating start vertex with all others.
    levels = [-1 for _ in range(len(graph))]
    # Mark as 0 the separation between the start vertex
    levels[0] = 0
    # Start proccesing all vertex in queue
    while queue:
        # Proccess the first (FIFO) vertex in queue.
        s = queue.popleft()
        # Check all neightbours
        for i in graph[s]:
            # If the node is not visited yet, add to queue and mark as visited
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
            # Mark new separation between start vertex with all others
            if levels[i] < 0:
                levels[i] = levels[s] + 1
    print(levels)
    # Check if theres not a connection between other vertex or a separation of more than 6.
    for el in levels:
        if el == -1 or el > 6:
            return False
    return True
