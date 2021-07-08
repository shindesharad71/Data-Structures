# Construct BST from its given level order traversal
# https://www.geeksforgeeks.org/construct-bst-given-level-order-traversal/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def level_order(root: Node, data):
    if root is None:
        root = Node(data)
        return root

    if data <= root.data:
        root.left = level_order(root.left, data)
    else:
        root.right = level_order(root.right, data)

    return root


def construct_bst(arr, n):
    if n == 0:
        return None

    root = None

    for i in range(0, n):
        root = level_order(root, arr[i])

    return root


def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Driver program
if __name__ == "__main__":
    arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
    n = len(arr)

    root = construct_bst(arr, n)

    print("Inorder Traversal: ", end="")
    inorder(root)
