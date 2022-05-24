from graph_utils import remove_all_edges
from random import choice, sample


def vertex_cover_ra4(graph: dict) -> tuple:
    vertex_cover = set()
    finished, origin, destiny = _get_random_edge(graph)
    while finished:
        picked_vertex = choice([origin, destiny])
        graph = remove_all_edges(graph, picked_vertex)
        vertex_cover.add(picked_vertex)
        finished, origin, destiny = _get_random_edge(graph)
    return vertex_cover, len(vertex_cover)


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
        if len(graph.keys()) > 0:
            random_origin_vertex = sample(all_processed, 1)[0]
            all_processed.remove(random_origin_vertex)
            if len(graph[random_origin_vertex]) > 0:
                random_destiny_vertex = sample(
                    graph[random_origin_vertex], 1)[0]
                found = True
        else:
            found = False
    return found, random_origin_vertex, random_destiny_vertex
