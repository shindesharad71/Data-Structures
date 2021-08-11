# Find k-cores of an undirected graph
# https://www.geeksforgeeks.org/find-k-cores-graph/

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, v, visited, vDegree, k):
        visited.add(v)

        for i in self.graph[v]:
            if vDegree[v] < k:
                vDegree[i] = vDegree[i] - 1

            if i not in visited:
                self.DFSUtil(i, visited, vDegree, k)

    def PrintKCores(self, k):
        visit = set()
        degree = defaultdict(lambda: 0)

        for i in list(self.graph):
            degree[i] = len(self.graph[i])

        for i in list(self.graph):
            if i not in visit:
                self.DFSUtil(i, visit, degree, k)

        for i in list(self.graph):
            if degree[i] >= k:
                print(str("\n [ ") + str(i) + str(" ]"), end=" ")

                for j in self.graph[i]:
                    if degree[j] >= k:
                        print("-> " + str(j), end=" ")
                print()
