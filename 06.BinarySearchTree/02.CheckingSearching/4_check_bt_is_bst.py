# A program to check if a binary tree is BST or not
# https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = self.right = None


def is_bst_util(root: Node, prev: Node) -> bool:
    if root:

        # traverse the tree in inorder fashion
        # and keep track of prev node
        if is_bst_util(root.left, prev):
            return False

        # Allows only distinct value nodes
        if prev is not None and root.data <= prev.data:
            return False

        prev = root

        return is_bst_util(root.right, prev)

    return True


def is_bst(root: Node) -> bool:
    prev = None
    return is_bst_util(root, prev)


# Driver Code
if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.right.left = Node(1)
    root.right.right = Node(3)

    if is_bst(root) is None:
        print("Is BST")
    else:
        print("Not a BST")
