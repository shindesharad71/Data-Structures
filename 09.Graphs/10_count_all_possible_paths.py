# Count all possible paths between two vertices
# https://www.geeksforgeeks.org/count-possible-paths-two-vertices/


class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(v)]

    def addEdge(self, u, v):
        self.adj[u].append(v)

    def countPaths(self, s, d):
        visited = [False] * self.v

        pathCount = [0]

        self.countPathsUtil(s, d, visited, pathCount)

        return pathCount[0]

    def countPathsUtil(self, u, d, visited, pathCount):
        visited[u] = True

        if u == d:
            pathCount[0] += 1

        else:
            i = 0
            while i < len(self.adj[u]):
                if not visited[self.adj[u][i]]:
                    self.countPathsUtil(self.adj[u][i], d, visited, pathCount)

                i += 1

        visited[u] = False
