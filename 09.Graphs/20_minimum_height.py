# Roots of a tree which give minimum height
# https://www.geeksforgeeks.org/roots-tree-gives-minimum-height/

# Python program to find root which gives minimum
# height to tree

# This class represents a undirected graph using
# adjacency list representation

from queue import *


class Graph:

    # Constructor of graph, initialize adjacency list
    # and degree vector
    def __init__(self, V, addEdge, rootForMinimumHeight):
        self.V = V
        self.adj = dict((i, []) for i in range(V))
        self.degree = list()
        for i in range(V):
            self.degree.append(0)

        # The below lines allows us define methods outside
        # of class definition
        # Check http://bit.ly/2e5HfrW for better explanation
        Graph.addEdge = addEdge
        Graph.rootForMinimumHeight = rootForMinimumHeight


# addEdge method adds vertex to adjacency list and
# increases degree by 1
def addEdge(self, v, w):
    self.adj[v].append(w)  # Adds w to v's list
    self.adj[w].append(v)  # Adds v to w's list
    self.degree[v] += 1  # increment degree of v by 1
    self.degree[w] += 1  # increment degree of w by 1


# Method to return roots which gives minimum height to tree
def rootForMinimumHeight(self):
    q = Queue()

    # First enqueue all leaf nodes in queue
    for i in range(self.V):
        if self.degree[i] == 1:
            q.put(i)

    # loop until total vertex remains less than 2
    while self.V > 2:
        p = q.qsize()
        self.V -= p
        for i in range(p):
            t = q.get()

            # for each neighbour, decrease its degree and
            # if it become leaf, insert into queue
            for j in self.adj[t]:
                self.degree[j] -= 1
                if self.degree[j] == 1:
                    q.put(j)

    # Copying the result from queue to result vector
    res = list()
    while q.qsize() > 0:
        res.append(q.get())

    return res


# Driver code
if __name__ == "__main__":
    g = Graph(6, addEdge, rootForMinimumHeight)
    g.addEdge(0, 3)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(4, 3)
    g.addEdge(5, 4)

    # Function call
    res = g.rootForMinimumHeight()
    for i in res:
        print(i)
