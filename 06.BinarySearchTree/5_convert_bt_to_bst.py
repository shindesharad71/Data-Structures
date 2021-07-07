# Binary Tree to Binary Search Tree Conversion
# https://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/

# Binary Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def store_inorder(root: Node, arr: list) -> None:
    if root:
        store_inorder(root.left, arr)
        arr.append(root.data)
        store_inorder(root.right, arr)


def count_nodes(root: Node) -> int:
    if root is None:
        return 0

    return count_nodes(root.left) + count_nodes(root.right) + 1


def arr_to_bst(arr: list, root: Node):
    if root is None:
        return

    arr_to_bst(arr, root.left)

    if len(arr) > 0:
        root.data = arr[0]
        arr.pop(0)

    arr_to_bst(arr, root.right)


def bt_to_bst(root: Node):
    if root is None:
        return

    arr = []
    store_inorder(root, arr)

    arr_to_bst(arr, root)

    arr.sort()

    arr_to_bst(arr, root)


def print_inorder(root: Node):
    if root:
        print_inorder(root.left)
        print(root.data, end=" ")
        print_inorder(root.right)


# Driver Code
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)

    # Convert binary tree to BST
    bt_to_bst(root)

    print("Following is the inorder traversal of the converted BST")
    print_inorder(root)
