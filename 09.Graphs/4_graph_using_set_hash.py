# Graph representations using set and hash
# https://www.geeksforgeeks.org/graph-representations-using-set-hash/


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = dict()

    # Adds an edge to undirected graph
    def add_edge(self, source, destination):
        # Add an edge from source to destination.
        # A new element is inserted to adjacent
        # list of source.
        if source not in self.graph:
            self.graph = {destination}
        else:
            self.graph.add(destination)

        if destination not in self.graph:
            self.graph[destination] = {source}
        else:
            self.graph[destination].add(source)

    def print_graph(self):
        for i, adjlist in sorted(self.graph.items()):
            print("Adjacency of vertex ", i)
            for j in sorted(adjlist, reverse=True):
                print(j, end=" ")

    def search_edges(self, source, destination):
        if source in self.graph:
            if destination in self.graph:
                print(f"Edge form {source} to {destination} found")
            else:
                print(f"Edge form {source} to {destination} not found")

        else:
            print(f"Source vertex {source} is not present in graph")


# Driver code
if __name__ == "__main__":

    g = Graph(5)

    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    # Print adjacency list
    # representation of graph
    g.print_graph()

    # Search the given edge in a graph
    g.search_edges(2, 1)
    g.search_edges(0, 3)
