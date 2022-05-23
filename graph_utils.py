
# Lee el archivo de la ruta especificada en el parametro
# y retorna un grafo que lo representa
def read_graph(path):
    graph = {}
    file = open(path, "r")
    lines = file.readlines()
    
    for line in lines:
        parsed = line.replace("\n", "").split("\t")
        u = int(parsed[0])
        v = int(parsed[1])

        u_links = graph.get(u, set())
        u_links.add(v)
        graph[u] = u_links

        v_links = graph.get(v, set())
        v_links.add(u)
        graph[v] = v_links
    
    return graph

# Elimina todos los ejes de un vertice dado
def remove_all_edges(graph, vertex):
    new_graph = graph.copy()
    new_graph[vertex] = []
    for u in graph.keys():
        if u != vertex:
            new_list = new_graph[u]
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
