# Elimina todos los ejes de un vertice dado
# in situ
def _remove_all_edges(graph, vertex):
    graph[vertex] = set()
    for u in graph:
        graph[u].discard(vertex)


def _get_greatest_degree_vertex(graph):
    """
        Retorna el vertice de mayor grado del grafo dado
        Retorna None cuando todos los vertices tienen grado 0,
          o lo que es lo mismo, cuando no hay mas ejes por validar
    """
    max_degree_vertex = None
    max_degree_value = 0

    for u in graph:
        degree = len(graph[u])
        if degree > max_degree_value:
            max_degree_vertex = u
            max_degree_value = degree
        
    return max_degree_vertex


def vertex_cover_aa2(graph):
    """
        Escoger el vertice de mayor grado, descartar los ejes que llegan al vertice
        escogido y repetir hasta que no queden ejes.
    """
    print("Entró a vertex_cover_aa2")
    answer = set()

    # 1. Escoger el vertice de mayor grado
    greatest_degree_vertex = _get_greatest_degree_vertex(graph)

    while greatest_degree_vertex != None:
        answer.add(greatest_degree_vertex)
        # 2. Descartar los ejes que llegan al vertice
        _remove_all_edges(graph, greatest_degree_vertex)
        # 3. Repetir hasta que no queden ejes
        greatest_degree_vertex = _get_greatest_degree_vertex(graph)

    print("Respuesta:", answer, len(answer))
    return answer
