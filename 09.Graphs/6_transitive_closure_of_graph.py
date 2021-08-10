# Transitive Closure of a Graph using DFS
# https://www.geeksforgeeks.org/transitive-closure-of-a-graph-using-dfs/

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.v = vertices
