from random import choice, sample
import time


# Elimina todos los ejes de un vertice dado
def remove_all_edges(graph, vertex):
    new_graph = graph.copy()
    new_graph[vertex] = set()

    for u in graph.keys():
        if u != vertex:
            if u in new_graph:
                new_graph[u].discard(vertex)
                
    return new_graph


# Elimina un unico eje
def remove_edge(graph, first_vertex, second_vertex):
    new_graph = graph.copy()

    new_first_list = new_graph[first_vertex]
    new_first_list.remove(second_vertex)
    new_graph[first_vertex] = new_first_list

    new_second_list = new_graph[second_vertex]
    new_second_list.remove(first_vertex)
    new_graph[second_vertex] = new_second_list

    return new_graph


def _get_random_edge(graph: dict) -> tuple:
    """
        Selecciona aleatoriamente un eje
        Si no quedan ejes para escoger, retorna False, None, None
    """
    found = False
    random_origin_vertex = None
    random_destiny_vertex = None
    all_processed = set(graph.keys())
    while not found and len(all_processed) > 0:
        random_origin_vertex = sample(all_processed, 1)[0]
        all_processed.remove(random_origin_vertex)
        if len(graph[random_origin_vertex]) > 0:
            random_destiny_vertex = sample(graph[random_origin_vertex], 1)[0]
            found = True
    return found, random_origin_vertex, random_destiny_vertex


def vertex_cover_4(graph: dict) -> tuple:
    tiempo_inicio = time.time()
    vertex_cover = set()
    finished, origin, destiny = _get_random_edge(graph)
    while finished:
        picked_vertex = choice([origin, destiny])
        graph = remove_all_edges(graph, picked_vertex)
        vertex_cover.add(picked_vertex)
        finished, origin, destiny = _get_random_edge(graph)

    tiempo_fin = time.time()
    return vertex_cover, tiempo_fin - tiempo_inicio

