# Level of Each node in a Tree from source node (using BFS)
# https://www.geeksforgeeks.org/level-node-tree-source-node-using-bfs/

import queue


def printLevels(graph, v, x):
    level = [None] * v
    marked = [False] * v

    que = queue.Queue()

    que.put(x)

    level[x] = 0

    marked[x] = True

    while not que.empty():
        x = que.get()

        for i in range(len(graph[x])):
            b = graph[x][i]

            if not marked[b]:
                que.put(b)

                level[b] = level[x] + 1

                marked[b] = True

    # display all nodes and their levels
    print("Nodes", " ", "Level")
    for i in range(V):
        print(" ", i, " --> ", level[i])
