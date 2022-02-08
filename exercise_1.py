from collections import deque

def bfs_with_level(graph):
    visited = [False for _ in range(len(graph))]
    queue = deque()
    queue.append(0)
    visited[0] = True
    levels = [-1 for _ in range(len(graph))]
    levels[0] = 0
    while queue:
        s = queue.popleft()
        for i in graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
            if levels[i] < 0:
                levels[i] = levels[s] + 1
    print(levels)
    for el in levels:
        if el == -1 or el > 6:
            return False
    return True
