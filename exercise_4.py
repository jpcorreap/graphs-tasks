# 4. Dada una base de datos con los costos de todos los vuelos del mundo, encontrar la serie de
# vuelos que con el menor costo posible nos permitan viajar desde Bogotá hacia la ciudad en la
# que queremos tomar vacaciones.

def minDistance(dist, queue):
    minimum = float("Inf")
    min_index = -1
    for i in range(len(dist)):
        if dist[i] < minimum and i in queue:
            minimum = dist[i]
            min_index = i
    return min_index


def dijkstra(graph, src, dest):
    V = len(graph)
    # Keep track distance from source to all other vertex using dist array.
    dist = [float("Inf")] * V
    # Keep in track the parent node for the path reconstruction
    parent = [-1] * V
    # Mark as 0 the distance from source
    dist[src] = 0
    # Queue for proccessing all vertex, add all vertex to queue.
    queue = []
    for i in range(V):
        queue.append(i)
    # While there are vertex to proccess
    while queue:
        # Find minimun distance from proccesed vertex to all other neightbours
        u = minDistance(dist, queue)
        # Mark as proccesed
        queue.remove(u)
        # If we process destination node, algorithm is complete.
        if u == dest:
            break
        # Check for each vertex if it is necessary to update the parent and distance arrays
        for i in range(V):
            if graph[u][i] and i in queue:
                if dist[u] + graph[u][i] < dist[i]:
                    dist[i] = dist[u] + graph[u][i]
                    parent[i] = u
    return printSolution(dist, parent, dest, src)


def printPath(parent, j):
    ans = ""
    if parent[j] == -1:
        return ""
    ans += printPath(parent, parent[j])
    ans += f"{j}->"
    return ans


def printSolution(dist, parent, dest, src):
    ans = ""
    ans += f"Minima distancia entre la ciudad {src} y la ciudad {dest}: {dist[dest]}\n"
    ans_parent = printPath(parent, dest)[:-2]
    ans += f"Serie de vuelos: {src}->{ans_parent}"
    ans_parent = [int(x) for x in ans_parent.split('->')]
    answer = [src, *ans_parent]
    print(ans)
    return answer
