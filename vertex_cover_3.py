
from graph_utils import remove_all_edges

def vertex_cover_aa3(graph: dict) -> set:
    V = len(graph)
    vertex_cover = set()
    for vertex in range(V):
        if vertex in graph:
            if len(graph[vertex]) > 1:
                for vertex_2 in graph[vertex]:
                    break
                max_vertex = -1
                if len(graph[vertex]) > len(graph[vertex_2]):
                    max_vertex = vertex
                else:
                    max_vertex = vertex_2
                graph = remove_all_edges(graph, max_vertex)
                vertex_cover.add(max_vertex)
    return vertex_cover, len(vertex_cover)