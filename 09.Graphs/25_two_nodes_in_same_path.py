# Check if two nodes are on same path in a tree
# https://www.geeksforgeeks.org/check-if-two-nodes-are-on-same-path-in-a-tree/


def dfs(graph, v):
    global intime, outtime, visit, MAX, timer
    visit.add(v)

    # Increment the timer as you enter
    # the recursion for v
    timer += 1

    # Upgrade the in time for the vertex
    intime[v] = timer
    it = 0
    while it < len(graph[v]):
        if graph[v][it] not in visit:
            dfs(graph, graph[v][it])
        it += 1

    # increment the timer as you
    # exit the recursion for v
    timer += 1

    # upgrade the outtime for that node
    outtime[v] = timer


# Returns true if 'u' and 'v' lie on
# same root to leaf path else false.
def query(u, v):
    global intime, outtime, visit, MAX, timer
    return (intime[u] < intime[v] and outtime[u] > outtime[v]) or (
        intime[v] < intime[u] and outtime[v] > outtime[u]
    )


# Driver code
if __name__ == "__main__":
    MAX = 100001

    # To keep track of visited vertices in DFS
    visit = set()

    # To store start and end time of
    # all vertices during DFS.
    intime = [0] * MAX
    outtime = [0] * MAX

    # initially timer is zero
    timer = 0

    # Let us create above shown tree
    n = 9  # total number of nodes
    graph = [[] for i in range(n + 1)]
    graph[1].append(2)
    graph[1].append(3)
    graph[3].append(6)
    graph[2].append(4)
    graph[2].append(5)
    graph[5].append(7)
    graph[5].append(8)
    graph[5].append(9)

    # Start dfs (here root node is 1)
    dfs(graph, 1)

    # below are calls for few pairs of nodes
    print("Yes") if query(1, 5) else print("No")
    print("Yes") if query(2, 9) else print("No")
    print("Yes") if query(2, 6) else print("No")
