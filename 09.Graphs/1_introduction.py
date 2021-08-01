# Graph and its representations
# https://www.geeksforgeeks.org/graph-and-its-representations/

# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None
