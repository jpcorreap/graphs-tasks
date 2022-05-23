graph = {
    0: [3, 4],
    1: [2, 5],
    2: [1, 3],
    3: [0, 2, 4, 5],
    4: [0, 3, 5],
    5: [1, 3, 4]
}

# Elimina todos los ejes de un vertice dado
def remove_all_edges(graph, vertex):
    new_graph = graph.copy()
    new_graph[vertex] = []
    for u in graph.keys():
        if u != vertex:
            new_list = new_graph[u]
            if vertex in new_list:
                new_list.remove(vertex)
                new_graph[u] = new_list
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


print(remove_all_edges(graph, 1))