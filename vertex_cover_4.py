from collections import deque
import random

graph = {
    0: [3, 4],
    1: [2, 5],
    2: [1, 3],
    3: [0, 2, 4, 5],
    4: [0, 3, 5],
    5: [1, 3, 4]
}


def vertex_cover_aa4(graph):

    #Escoger aleatoriamente un eje
    verticeOrigen = random.randint(0, len(graph)-1)
    numEjes = len(graph[verticeOrigen])
    verticeDestino = graph[verticeOrigen][random.randint(0, numEjes-1)]
    print("Eje escogido: {}-{}".format(verticeOrigen, verticeDestino))

    #Escoger aletoriamente un vertice
    binario = random.randint(0, 1)
    if binario == 0:
        vertice = verticeOrigen
    else:
        vertice = verticeDestino
    print("Vertice escogido:", vertice)

    return True


vertex_cover_aa4(graph)