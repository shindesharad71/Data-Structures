# Depth First Search or DFS for a Graph
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

from collections import defaultdict


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=" ")

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)


# Driver code
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.DFS(2)
