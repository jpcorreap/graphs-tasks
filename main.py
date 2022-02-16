"""
 Implementar en grupos de 3 personas la solución utilizando el algoritmo de Edmond Karp para
 resolver el problema de encontrar la máxima cantidad de emparejamientos entre un grupo de personas
 y un grupo de trabajos. El programa debe recibir un archivo de entrada con las siguientes especificaciones:

 - La primera linea debe tener la cantidad de personas M y la cantidad de trabajos N.
 - Las siguientes lineas tiene dos números. El primero es un id de persona (de 0 a M-1) y el segundo es un id de
   trabajo (de 0 a N-1). La linea indica que la persona i puede hacer el trabajo j.
 - El programa debe imprimir un archivo que indiqué qué persona haría qué trabajo, de modo que se maximice la
   cantidad de trabajos a realizar.

Referencia: https://github.com/anxiaonong/Maxflow-Algorithms/blob/master/Edmonds-Karp%20Algorithm.py
"""
from os import path
"""
DFS that returns true if theres posible a matching between person i and every job other job j.
"""


def dfs_mod(i, match, seen, graph):
    for j in range(len(graph[0])):
        # If person i can do job j and j is not proccesed yet.
        if graph[i][j] and seen[j] == False:
            seen[j] = True  # Mark v as visited
            # If job v is not done by someone or
            # previously assigned person for job v (match[v]) has an alternate job available, mark job v to person v.
            if match[j] == -1 or dfs_mod(match[j], match, seen, graph):
                match[j] = i
                return True
    return False


"""
Main function that process max flow in maximum matching problem.
"""


def maximum_matching_max_flow(graph: list, file_name: str) -> None:
    jobs: int = len(graph[0])
    people: int = len(graph)
    # Array to keep a job done by a person. matching[i] 0<=i<jobs means the person matching[i] is asigned to job i.
    # Initialize in -1 if (no matching)
    matching: list = [-1 for _ in range(jobs)]
    for i in range(people):
        # Mark all jobs as not seen for next person.
        seen = [False for _ in range(jobs)]
        # Find if the person i can get a job with dfs
        dfs_mod(i, matching, seen, graph)
    file = open(f"output/output_{file_name}", "w")
    for job, person in enumerate(matching):
        if person != -1:
            file.write(f"{person} {job}\n")
    file.close()


def create_graph() -> tuple:
    print("Write the file name to test: (Add extension .txt)")
    file_name: str = input()
    while not path.isfile(f"input/{file_name}") and ".txt" in file_name:
        print("Incorrect file name, try again:")
        file_name: str = input()
    with open(f"input/{file_name}", "r") as file:
        people, jobs = map(int, file.readline().strip().split())
        graph: list = [[0 for _ in range(jobs)] for __ in range(people)]
        for line in file.readlines():
            person, job = map(int, line.strip().split())
            graph[person][job] = 1
    return (graph, file_name)


if __name__ == "__main__":
    graph, file_name = create_graph()
    maximum_matching_max_flow(graph, file_name)
