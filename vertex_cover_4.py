from graph_utils import remove_all_edges
import random


def vertex_cover_ra4(graph):
    # Variables
    rta = []
    vertices = []
    for i in range(len(graph)):
        vertices.append(i)

    while(len(vertices) != 0):
        # Escoger aleatoriamente un eje
        verticeOrigen = random.choice(vertices)
        while len(graph[verticeOrigen]) == 0:
            vertices.remove(verticeOrigen)
            if len(vertices) == 0:
                return rta
            verticeOrigen = random.choice(vertices)
        verticeDestino = random.choice(graph[verticeOrigen])
        print("Eje escogido: {}-{}".format(verticeOrigen, verticeDestino))

        # Escoger aletoriamente un vertice
        binario = random.randint(0, 1)
        if binario == 0:
            vertice = verticeOrigen
        else:
            vertice = verticeDestino
        print("Vertice escogido:", vertice)
        rta.append(vertice)
        vertices.remove(vertice)

        # Descartar ejes del vertice
        graph = remove_all_edges(graph, vertice)

    return rta
