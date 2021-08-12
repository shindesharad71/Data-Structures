# Iterative Depth First Traversal of Graph
# https://www.geeksforgeeks.org/iterative-depth-first-traversal/


class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(v)]

    def addEdge(self, v, w):
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


# Driver Code
if __name__ == "__main__":
    g = Graph(5)  # Total 5 vertices in graph
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 4)

    print("Following is Depth First Traversal")
    g.DFS(0)
