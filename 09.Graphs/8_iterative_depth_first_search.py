# Iterative Depth First Traversal of Graph
# https://www.geeksforgeeks.org/iterative-depth-first-traversal/


class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(v)]
