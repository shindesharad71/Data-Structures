# Convert a BST to a Binary Tree such that sum of all greater keys is added to every key
# https://www.geeksforgeeks.org/convert-bst-to-a-binary-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def add_greater_util(root: Node, sum_ptr):
    if root is None:
        return

    add_greater_util(root.right, sum_ptr)

    sum_ptr[0] = sum_ptr[0] + root.data

    root.data = sum_ptr[0]

    add_greater_util(root.left, sum_ptr)


def add_greater(root: Node):
    sum_ptr = [0]
    add_greater_util(root, sum_ptr)


def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Driver Code
if __name__ == "__main__":
    # Create following BST
    #         5
    #     / \
    #     2     13
    root = Node(5)
    root.left = Node(2)
    root.right = Node(13)

    print("Inorder traversal of the given tree")
    inorder(root)

    add_greater(root)
    print()
    print("Inorder traversal of the modified tree")
    inorder(root)
