# Height of a generic tree from parent array
# https://www.geeksforgeeks.org/height-generic-tree-parent-array/

# Python3 code to find height
# of N-ary tree in O(n)
from collections import deque

MAX = 1001

# Adjacency list to
# store N-ary tree
adj = [[] for i in range(MAX)]


# Build tree in tree in O(n)
def build_tree(arr, n):
    root_index = 0

    # Iterate for all nodes
    for i in range(n):

        # if root node, store
        # index
        if arr[i] == -1:
            root_index = i
        else:
            adj[i].append(arr[i])
            adj[arr[i]].append(i)

    return root_index


# Applying BFS
def BFS(start):
    # map is used as visited
    # array
    vis = {}

    q = deque()
    max_level_reached = 0

    # height of root node is
    # zero
    q.append([start, 0])

    # p.first denotes node in
    # adjacency list
    # p.second denotes level of
    # p.first
    p = []

    while len(q) > 0:
        p = q.popleft()
        vis[p[0]] = 1

        # store the maximum level
        # reached
        max_level_reached = max(max_level_reached, p[1])

        for i in range(len(adj[p[0]])):

            # adding 1 to previous level
            # stored on node p.first
            # which is parent of node
            # adj[p.first][i]
            # if adj[p.first][i] is not visited
            if adj[p[0]][i] not in vis:
                q.append([adj[p[0]][i], p[1] + 1])

    return max_level_reached


# Driver code
if __name__ == "__main__":
    # node 0 to node n-1
    parent = [-1, 0, 1, 2, 3]

    # Number of nodes in tree
    n = len(parent)

    root_index = build_tree(parent, n)
    ma = BFS(root_index)
    print("Height of N-ary Tree=", ma)
