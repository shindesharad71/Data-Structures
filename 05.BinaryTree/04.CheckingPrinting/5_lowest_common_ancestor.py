# Lowest Common Ancestor in a Binary Tree
# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def find_lca(root: Node, n1, n2):
    if root is None:
        return None

    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if root.data == n1 or root.data == n2:
        return root

    # Look for keys in left and right subtrees
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)

    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("LCA(4,5) = ", find_lca(root, 4, 5).data)
    print("LCA(4,6) = ", find_lca(root, 4, 6).data)
    print("LCA(3,4) = ", find_lca(root, 3, 4).data)
    print("LCA(2,4) = ", find_lca(root, 2, 4).data)
