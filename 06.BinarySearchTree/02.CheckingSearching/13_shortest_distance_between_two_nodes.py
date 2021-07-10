# Shortest distance between two nodes in BST
# https://www.geeksforgeeks.org/shortest-distance-between-two-nodes-in-bst/


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = self.right = None


# Inserts node
def insert(root: Node, data: int) -> Node:
    if root is None:
        root = Node(data)
    elif data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root


# This function returns distance of x from
# root. This function assumes that x exists
# in BST and BST is not NULL.
def distance_from_root(root: Node, x: int) -> int:
    if root.data == x:
        return 0
    elif root.data > x:
        return 1 + distance_from_root(root.left, x)
    return 1 + distance_from_root(root.right, x)


# Returns minimum distance between a and b.
# This function assumes that a and b exist
# in BST.
def distance_between_two(root: Node, a: int, b: int) -> int:
    if root is None:
        return 0

    # If both keys lies in left
    if root.data > a and root.data > b:
        return distance_between_two(root.left, a, b)

    # If both keys lies in right
    if b > root.data and a > root.data:
        return distance_between_two(root.right, a, b)

    # Lie in opposite directions
    # (Root is LCA of two nodes)
    if a <= root.data <= b:
        return distance_from_root(root, a) + distance_from_root(root, b)


# This function make sure that a is smaller
# than b before making a call to distance_between_two()
def find_distance(root: Node, a: int, b: int):
    if a > b:
        a, b = b, a
    return distance_between_two(root, a, b)


# Driver code
if __name__ == "__main__":
    root = None
    root = insert(root, 20)
    insert(root, 10)
    insert(root, 5)
    insert(root, 15)
    insert(root, 30)
    insert(root, 25)
    insert(root, 35)
    a, b = 5, 55
    print(find_distance(root, 5, 35))
