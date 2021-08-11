# Find k-cores of an undirected graph
# https://www.geeksforgeeks.org/find-k-cores-graph/

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
