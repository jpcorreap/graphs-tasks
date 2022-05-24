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


def vertex_cover_1(original_graph):
    """
        Escoger arbitrariamente un eje, incluir los dos vertices
        conectados, descartar todos los demas ejes conectados por
        los vertices escogidos y repetir hasta que no queden ejes.
    """
    answer = set()
    graph = _transform_graph(original_graph)
    print(graph)
    # 1. Escoger arbitrariamente un eje
    arbitrary_edge = _get_arbitrary_edge(graph)

    while arbitrary_edge:
        print("arbitrary_edge", arbitrary_edge)
        u, v = arbitrary_edge
        # 2. Incluir los dos vertices conectados
        answer.add(u)
        answer.add(v)
        # 3. Descartar todos los demas ejes conectados por los vertices escogidos
        _remove_all_edges(graph, u)
        _remove_all_edges(graph, v)
        # Repetir hasta que no queden ejes
        arbitrary_edge = _get_arbitrary_edge(graph)

    print("Respuesta:", answer, len(answer))
    return answer
