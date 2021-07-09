# Find k-th smallest element in BST (Order Statistics in BST)
# https://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-statistics-in-bst/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def insert(root: Node, data: int):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# A simple inorder traversal based Python3
# program to find k-th smallest element
# in a BST.
def kth_smallest(root: Node):
    global k

    # Base case
    if root is None:
        return None

    # Search in left subtree
    left = kth_smallest(root.left)

    # If k'th smallest is found in
    # left subtree, return it
    if left is not None:
        return left

    # If current element is k'th
    # smallest, return it
    k -= 1
    if k == 0:
        return root

    # Else search in right subtree
    return kth_smallest(root.right)


# Function to find k'th largest element in BST
def print_kth_smallest(root: Node):
    res = kth_smallest(root)

    if res is None:
        print("There are less than k nodes in the BST")
    else:
        print("K-th Smallest Element is ", res.data)


# Driver code
if __name__ == "__main__":

    root = None
    keys = [20, 8, 22, 4, 12, 10, 14]

    for x in keys:
        root = insert(root, x)

    k = 3
    print_kth_smallest(root)
