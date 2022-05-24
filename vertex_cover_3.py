import time


def _transform_graph(graph):
    """
        Transforma un grafo que es un map de sets
        y retorna una lista de listas
    """
    new_graph = [[]]*len(graph)

    for vertex in graph:
        connections = list(graph[vertex])
        new_graph[vertex] = sorted(connections)
    
    return new_graph


# Elimina todos los ejes de un vertice dado
# in situ
def _remove_all_edges(graph, vertex):
    graph[vertex] = []
    for u in range(len(graph)):
        # Tries to remove the desired vertex 
        try:
            graph[u].remove(vertex)
        except ValueError:
            # If vertex is not connected, then do nothing
            pass 


def _get_arbitrary_edge(graph):
    """
        Selecciona arbitrariamente un eje, que corresponde al
        vertice de menor numero que aun tiene conexiones a otros vertices.
        Si no quedan ejes para escoger, retorna False
    """
    u = 0
    while u < len(graph):
        if len(graph[u]):
            return u, graph[u][0]
        u += 1
    return False


def vertex_cover_3(original_graph: dict) -> tuple:
    vertex_cover = set()
    graph = _transform_graph(original_graph)

    tiempo_inicio = time.time()
    # 1. Escoger arbitrariamente un eje
    arbitrary_edge = _get_arbitrary_edge(graph)

    while arbitrary_edge:
        u, v = arbitrary_edge
        max_vertex = u if len(graph[u]) > len(graph[v]) else v
        _remove_all_edges(graph, max_vertex)
        vertex_cover.add(max_vertex)
        arbitrary_edge = _get_arbitrary_edge(graph)
    
    tiempo_fin = time.time()
    return vertex_cover, tiempo_fin - tiempo_inicio
