# BFS using vectors & queue as per the algorithm of CLRS
# https://www.geeksforgeeks.org/bfs-using-vectors-queue-per-algorithm-clrs/

# Python3 program to implement BFS as
# per CLRS algorithm.
import queue


# This function adds an edge to the graph.
# It is an undirected graph. So edges
# are added for both the nodes.
def addEdge(g, u, v):
    g[u].append(v)
    g[v].append(u)


# This function does the Breadth
# First Search
def BFSSingleSource(g, s):
    # The Queue used for the BFS operation
    q = queue.Queue()

    # Pushing the root node inside
    # the queue
    q.put(s)

    # Distance of root node is 0 & colour is
    # gray as it is visited partially now
    d[s] = 0
    colour[s] = "green"

    # Loop to traverse the graph. Traversal
    # will happen traverse until the queue
    # is not empty.
    while not q.empty():

        # Extracting the front element(node)
        # and popping it out of queue.
        u = q.get()

        print(u, end=" ")

        # This loop traverses all the child
        # nodes of u
        i = 0
        while i < len(g[u]):

            # If the colour is white then
            # the said node is not traversed.
            if colour[g[u][i]] == "white":
                colour[g[u][i]] = "green"
                d[g[u][i]] = d[u] + 1
                p[g[u][i]] = u

                # Pushing the node inside queue
                # to traverse its children.
                q.put(g[u][i])
            i += 1

        # Now the node u is completely traversed
        # and colour is changed to black.
        colour[u] = "dark_green"


def BFSFull(g, n):
    # Initially all nodes are not traversed.
    # Therefore, the colour is white.
    colour = ["white"] * n
    d = [0] * n
    p = [-1] * n

    # Calling BFSSingleSource() for all
    # white vertices
    for i in range(n):
        if colour[i] == "white":
            BFSSingleSource(g, i)


# Driver Code
if __name__ == "__main__":
    # Graph with 7 nodes and 6 edges.
    n = 7

    # Declaring the vectors to store color,
    # distance and parent
    colour = [None] * n
    d = [None] * n
    p = [None] * n

    # The Graph vector
    g = [[] for i in range(n)]

    addEdge(g, 0, 1)
    addEdge(g, 0, 2)
    addEdge(g, 1, 3)
    addEdge(g, 1, 4)
    addEdge(g, 2, 5)
    addEdge(g, 2, 6)

    BFSFull(g, n)
