# Maximum number of edges to be added to a tree so that it stays a Bipartite graph
# https://www.geeksforgeeks.org/maximum-number-edges-added-tree-stays-bipartite-graph/


# Python 3 code to print maximum edges such
# that Tree remains a Bipartite graph
def dfs(adj, node, parent, color):

    # Increment count of nodes with
    # current color
    count_color[color] += 1

    # Traversing adjacent nodes
    for i in range(len(adj[node])):

        # Not recurring for the parent node
        if adj[node][i] != parent:
            dfs(adj, adj[node][i], node, not color)


# Finds maximum number of edges that
# can be added without violating
# Bipartite property.
def findMaxEdges(adj, n):

    # Do a DFS to count number of
    # nodes of each color
    dfs(adj, 1, 0, 0)

    return count_color[0] * count_color[1] - (n - 1)


# Driver code
if __name__ == "__main__":
    # To store counts of nodes with two colors
    count_color = [0, 0]
    n = 5
    adj = [[] for i in range(n + 1)]
    adj[1].append(2)
    adj[1].append(3)
    adj[2].append(4)
    adj[3].append(5)
    print(findMaxEdges(adj, n))
