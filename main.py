# Implementar en grupos de 3 personas la solución utilizando el algoritmo de Edmond Karp para resolver el problema
# de encontrar la máxima cantidad de emparejamientos entre un grupo de personas y un grupo de trabajos. El programa
# debe recibir un archivo de entrada con las siguientes especificaciones:
# 
# - La primera linea debe tener la cantidad de personas M y la cantidad de trabajos N.
# - Las siguientes lineas tiene dos números. El primero es un id de persona (de 0 a M-1) y el segundo es un id de
#   trabajo (de 0 a N-1). La linea indica que la persona i puede hacer el trabajo j.
# - El programa debe imprimir un archivo que indiqué qué persona haría qué trabajo, de modo que se maximice la
#   cantidad de trabajos a realizar.
#
# Entregar un archivo zip que contenga el código fuente de las soluciones a los problemas y un README.txt que
# indique cómo se deben ejecutar los programas implementados.

from utils import read_files

# Edmonds-Karp Algorithm
# Referencia: https://github.com/anxiaonong/Maxflow-Algorithms/blob/master/Edmonds-Karp%20Algorithm.py
def max_flow(C, s, t):
    n = len(C) # C is the capacity matrix
    F = [[0] * n for i in range(n)]
    path = bfs(C, F, s, t)
    #  print path
    while path != None:
        flow = min(C[u][v] - F[u][v] for u,v in path)
        for u,v in path:
            F[u][v] += flow
            F[v][u] -= flow
        path = bfs(C, F, s, t)
    return sum(F[s][i] for i in range(n))


# find path by using BFS
def bfs(C, F, s, t):
    queue = [s]
    paths = {s:[]}
    if s == t:
        return paths[s]
    while queue: 
        u = queue.pop(0)
        for v in range(len(C)):
            if(C[u][v]-F[u][v]>0) and v not in paths:
                paths[v] = paths[u]+[(u,v)]
                print(paths)
                if v == t:
                    return paths[v]
                queue.append(v)
    return None


# make a capacity graph
# node   s   o   p   q   r   t
C = [[ 0, 3, 3, 0, 0, 0 ],  # s
     [ 0, 0, 2, 3, 0, 0 ],  # o
     [ 0, 0, 0, 0, 2, 0 ],  # p
     [ 0, 0, 0, 0, 4, 2 ],  # q
     [ 0, 0, 0, 0, 0, 2 ],  # r
     [ 0, 0, 0, 0, 0, 3 ]]  # t


if __name__ == "__main__":
    source = 0  # A
    sink = 5    # F
    max_flow_value = max_flow(C, source, sink)
    print("Edmonds-Karp algorithm")
    print("max_flow_value is: ", max_flow_value)
    read_files()
