# Count the number of nodes at given level in a tree using BFS
# https://www.geeksforgeeks.org/count-number-nodes-given-level-using-bfs/

from collections import deque

adj = [[] for i in range(1001)]


def addEdge(v, w):
    adj[v].append(w)
    adj[w].append(v)


def BFS(s, l):
    v = 100

    visited = [False] * v

    level = [0] * v

    for i in range(v):
        visited[i] = False
        level[i] = 0

    queue = deque()

    visited[s] = True
    queue.append(s)
    level[s] = 0

    while len(queue):
        s = queue.popleft()

        for i in adj[s]:
            if not visited[i]:
                level[i] = level[s] + 1
                visited[i] = True
                queue.append(i)

    count = 0
    for i in range(v):
        if level[i] == l:
            count += 1

    return count


# Driver code
if __name__ == "__main__":
    # Create a graph given
    # in the above diagram
    addEdge(0, 1)
    addEdge(0, 2)
    addEdge(1, 3)
    addEdge(2, 4)
    addEdge(2, 5)

    level = 2

    print(BFS(0, level))
