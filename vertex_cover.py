
import sys
import time
from graph_utils import read_graph
from vertex_cover_1 import vertex_cover_aa1
from vertex_cover_4 import vertex_cover_aa4


ALGORITMOS = [
    vertex_cover_aa1,
    vertex_cover_aa1,
    vertex_cover_aa1,
    vertex_cover_aa4
]


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

    respuesta = []

    graph = read_graph(input_file_path)

    tiempo_inicio = time.time()
    respuesta = ALGORITMOS[algoritmo_a_ejecutar - 1](graph)
    tiempo_fin = time.time()

    print(respuesta)
    print(tiempo_fin - tiempo_inicio)
