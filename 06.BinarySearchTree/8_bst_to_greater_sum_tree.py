# Transform a BST to greater sum tree
# https://www.geeksforgeeks.org/transform-bst-sum-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def transform_tree_util(root: Node):
    if root is None:
        return

    transform_tree_util(root.right)

    global sum
    sum = sum + root.data

    root.data = sum - root.data

    transform_tree_util(root.left)


def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Driver Program to test above functions
if __name__ == "__main__":
    sum = 0
    root = Node(11)
    root.left = Node(2)
    root.right = Node(29)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(40)
    root.right.right.left = Node(35)

    print("Inorder Traversal of given tree")
    inorder(root)

    transform_tree_util(root)

    print("\nInorder Traversal of transformed tree")
    inorder(root)
