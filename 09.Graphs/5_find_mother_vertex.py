# Find a Mother Vertex in a Graph
# https://www.geeksforgeeks.org/find-a-mother-vertex-in-a-graph/

from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    # A recursive function to print DFS starting from v
    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    # Add w to the list of v
    def addEdge(self, v, w):
        self.graph[v].append(w)

    # Returns a mother vertex if exists. Otherwise returns -1
    def findMother(self):
        visited = [False] * self.v

        v = 0

        for i in range(self.v):
            if not visited[i]:
                self.DFSUtil(i, visited)
                v = i

        visited = [False] * self.v
        self.DFSUtil(v, visited)
        if any(i == False for i in visited):
            return -1
        else:
            return v


# Driver Code
if __name__ == "__main__":
    g = Graph(7)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(4, 1)
    g.addEdge(6, 4)
    g.addEdge(5, 6)
    g.addEdge(5, 2)
    g.addEdge(6, 0)
    print("A mother vertex is " + str(g.findMother()))
