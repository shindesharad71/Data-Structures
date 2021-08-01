# Graph and its representations
# https://www.geeksforgeeks.org/graph-and-its-representations/

# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [None] * self.v

    def add_edge(self, src, dest):
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.v):
            print(f"Adjacency list of vertex {i} head")
            temp = self.graph[i]
            while temp:
                print(f" -> {temp.vertex}", end=" ")
                temp = temp.next
            print(" \n")


# Driver Code
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
