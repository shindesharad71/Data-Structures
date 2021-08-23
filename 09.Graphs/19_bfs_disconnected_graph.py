# BFS for Disconnected Graph
# https://www.geeksforgeeks.org/bfs-disconnected-graph/

# Python3 implementation of modified BFS
import queue


# A utility function to add an edge
# in an undirected graph.
def addEdge(adj, u, v):
    adj[u].append(v)


# A utility function to do BFS of
# graph from a given vertex u.
def BFSUtil(u, adj, visited):
    # Create a queue for BFS
    q = queue.Queue()

    # Mark the current node as visited
    # and enqueue it
    visited[u] = True
    q.put(u)

    # 'i' will be used to get all adjacent
    # vertices 4 of a vertex list<int>::iterator i

    while not q.empty():

        # Dequeue a vertex from queue
        # and print it
        u = q.queue[0]
        print(u, end=" ")
        q.get()

        # Get all adjacent vertices of the
        # dequeued vertex s. If an adjacent
        # has not been visited, then mark
        # it visited and enqueue it
        i = 0
        while i != len(adj[u]):
            if not visited[adj[u][i]]:
                visited[adj[u][i]] = True
                q.put(adj[u][i])
            i += 1


# This function does BFSUtil() for all
# unvisited vertices.
def BFS(adj, V):
    visited = [False] * V
    for u in range(V):
        if not visited[u]:
            BFSUtil(u, adj, visited)


# Driver code
if __name__ == "__main__":
    V = 5
    adj = [[] for i in range(V)]

    addEdge(adj, 0, 4)
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 1, 4)
    addEdge(adj, 2, 3)
    addEdge(adj, 3, 4)
    BFS(adj, V)
