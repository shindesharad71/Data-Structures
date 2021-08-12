# Iterative Depth First Traversal of Graph
# https://www.geeksforgeeks.org/iterative-depth-first-traversal/


class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(v)]

    def adj(self, v, w):
        self.adj[v].append(w)

    def DFS(self, s):
        visited = [False for i in range(self.v)]

        stack = [s]

        while len(stack):
            s = stack[-1]
            stack.pop()

            if not visited[s]:
                print(s, end=" ")
                visited[s] = True

            for node in self.adj[s]:
                if not visited[node]:
                    stack.append(node)
