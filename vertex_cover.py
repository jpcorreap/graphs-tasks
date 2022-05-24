
import sys
import time
from vertex_cover_1 import vertex_cover_1
from vertex_cover_2 import vertex_cover_2
from vertex_cover_3 import vertex_cover_3
from vertex_cover_4 import vertex_cover_4


ALGORITMOS = [
    vertex_cover_1,
    vertex_cover_2,
    vertex_cover_3,
    vertex_cover_4
]


# Lee el archivo de la ruta especificada en el parametro
# y retorna un grafo que lo representa. Este grafo es un
# map de sets, algo del estilo {0:{1,2}, 1:{0}, 2:{0}}
def _read_graph(path):
    file = open(path, "r")
    lines = file.readlines()
    # Get number of vertices from first line
    number_of_vertices = int(lines.pop(0))
    
    graph = {x: set() for x in range(0, number_of_vertices)}

    for line in lines:
        parsed = line.replace("\n", "").split("\t")
        u = int(parsed[0])
        v = int(parsed[1])
        graph[u].add(v)
        graph[v].add(u)

    return graph


if __name__ == "__main__":
    """
        El programa debe recibir un archivo de texto con los ejes del grafo y un numero que indique
        el algoritmo a ejecutar. Cada linea del archivo debe contener una pareja de numeros que
        representan los dos vertices conectados, separados por tab. El programa no pueden hacer
        ninguna suposicion acerca del sistema operativo o del sistema de archivos del usuario.

        El programa debe imprimir los vertices del cubrimiento encontrado y el tamano del
        conjunto de vertices.
    """
    # Ruta al archivo con los ejes de entrada
    input_file_path = sys.argv[1]
    # Numero que indica el algoritmo a ejecutar
    algoritmo_a_ejecutar = int(sys.argv[2])
    graph = _read_graph(input_file_path)

    respuesta, tiempo_ejecucion = ALGORITMOS[algoritmo_a_ejecutar - 1](graph)

    # print("» Respuesta: ", respuesta)
    print("» Cantidad de vértices en la respuesta: ", len(respuesta))
    print("» Tiempo de ejecución: {} s".format(tiempo_ejecucion))
