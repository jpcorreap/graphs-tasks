import sys
import random


def main(argList):
    if "-edges" in argList:
        a = argList.index("-edges")
        edges = int(argList[a + 1])
    else:
        edges = 512

    if "-nodes" in argList:
        a = argList.index("-nodes")
        nodes = int(argList[a + 1])
    else:
        nodes = 128

    if "-seed" in argList:
        a = argList.index("-seed")
        seed = int(argList[a + 1])
    else:
        seed = 1048576
    write_str = ""
    for i in genPair(nodes, edges, seed):
        write_str += i
    with open("input10000.txt", "w") as file:
        file.write(write_str)
    
def genPair(nodes, edges, seed):
    graph = set()
    nodeList = range(nodes)
    random.seed(seed)
    while len(graph) < edges:
        pair = f"{str(random.choice(nodeList))}\t{str(random.choice(nodeList))}\n"
        graph.add(pair)

    return graph


if __name__ == "__main__":
    main(sys.argv[1:])
