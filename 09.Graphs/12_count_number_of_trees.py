# Count number of trees in a forest
# https://www.geeksforgeeks.org/count-number-trees-forest/


def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


def DFSUtil(u, adj, visited):
    visited[u] = True
    for i in range(len(adj[u])):
        if visited[adj[u][i]] == False:
            DFSUtil(adj[u][i], adj, visited)


def countTrees(adj, v):
    visited = [False] * v
    res = 0
    for u in range(v):
        if visited[u] == False:
            DFSUtil(u, adj, visited)
            res += 1
    return res


# Driver code
if __name__ == "__main__":

    V = 5
    adj = [[] for i in range(V)]
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 3, 4)
    print(countTrees(adj, V))
