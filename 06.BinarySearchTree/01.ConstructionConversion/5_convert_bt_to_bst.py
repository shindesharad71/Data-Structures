# Binary Tree to Binary Search Tree Conversion
# https://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/

# Binary Tree Node
class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = self.right = None


def store_inorder(root: Node, arr: list):
    if root:
        store_inorder(root.left, arr)
        arr.append(root.data)
        store_inorder(root.right, arr)


# Print the inorder traversal of the tree
def print_inorder(root: Node):
    if root:
        print_inorder(root.left)
        print(root.data, end=" ")
        print_inorder(root.right)


# Helper function that copies contents of sorted array
# to Binary tree
def arr_to_bst(arr, root):
    # Base Case
    if root is None:
        return

    # First update the left subtree
    arr_to_bst(arr, root.left)

    # now update root's data delete the value from array
    root.data = arr[0]
    arr.pop(0)

    # Finally update the right subtree
    arr_to_bst(arr, root.right)


# This function converts a given binary tree to BST
def bt_to_bst(root):
    # Base Case: Tree is empty
    if root is None:
        return

    # Create the temp array and store the inorder traversal
    # of tree
    arr = []
    store_inorder(root, arr)

    # Sort the array
    arr.sort()

    # copy array elements back to binary tree
    arr_to_bst(arr, root)


# Driver program to test above function
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
