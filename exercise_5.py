# 5. Una ciudad se diseño de tal modo que todas sus calles fueran de una sola vía. Con el paso
# del tiempo la cantidad de habitantes de la ciudad creció y esto produjo grandes trancones en
# algunas de las vias debido a algunos desvíos innecesarios que tienen que tomar los habitantes
# de la ciudad para poder llegar a sus trabajos. Por lo tanto, el alcalde tomó la decisión de
# ampliar algunas vias para que puedan convertirse en doble via. Dado el mapa de la ciudad y el
# costo de convertir cada via actual en doble via, determinar qué vias se deben convertir, de
# modo que se pueda transitar de cualquier punto a cualquier punto de la ciudad por dobles vias
# y que el costo de la conversión sea el mínimo posible.

# Referencia de la solucion: https://www.programiz.com/dsa/kruskal-algorithm


# Get set of i
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


# Joins two sets
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    # According to rank, one root become child of the other root
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


# Kruskal Algorithm to obtain MST
def KruskalMST(graph, V):
    # Result array for MST
    result = []
    i = 0
    e = 0
    graph = sorted(graph, key=lambda item: item[2])
    parent = []
    rank = []
    # Creates a partition for each node
    for node in range(V):
        parent.append(node)
        rank.append(0)

    # It will iterate over all edges
    while e < V - 1:
        u, v, w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        # It assures this union will not create a cycle
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y) # Joins two trees
    minimumCost = 0
    print("Vias a construir:")
    for u, v, weight in result:
        minimumCost += weight
        print(f"Debe mejorar la vía de {u} a {v}, con costo {weight}")
    print("Precio total de la inversión", minimumCost)
    return result
