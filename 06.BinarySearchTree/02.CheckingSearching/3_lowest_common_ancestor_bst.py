# Lowest Common Ancestor in a Binary Search Tree
# https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Function to find LCA of n1 and n2.
# The function assumes that both
#   n1 and n2 are present in BST
def find_lca(root: Node, n1: int, n2: int) -> Node:
    while root:
        # If both n1 and n2 are smaller than root,
        # then LCA lies in left
        if root.data > n1 and root.data > n2:
            root = root.left

        # If both n1 and n2 are greater than root,
        # then LCA lies in right
        elif root.data < n1 and root.data < n2:
            root = root.right

        else:
            break

    return root


if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    n1 = 10
    n2 = 14
    t = find_lca(root, n1, n2)
    print(f"LCA of {n1} and {n2} is {t.data}")

    n1 = 14
    n2 = 8
    t = find_lca(root, n1, n2)
    print(f"LCA of {n1} and {n2} is {t.data}")

    n1 = 10
    n2 = 22
    t = find_lca(root, n1, n2)
    print(f"LCA of {n1} and {n2} is {t.data}")
