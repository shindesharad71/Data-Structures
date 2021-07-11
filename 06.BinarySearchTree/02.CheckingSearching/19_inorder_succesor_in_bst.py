# Inorder Successor in Binary Search Tree
# https://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.data = key
        self.left = self.right = None


# A utility function to insert a new
# Node with given key in BST and also
# maintain count ,Sum
def insert(root: Node, key: int):
    # If the tree is empty, return a new Node
    if root is None:
        return Node(key)

    # Otherwise, recur down the tree
    if root.data > key:
        root.left = insert(root.left, key)

    elif root.data < key:
        root.right = insert(root.right, key)

    # return the (unchanged) Node pointer
    return root


# Given a non-empty binary search tree,
# return the minimum data value
# found in that tree. Note that the
# entire tree doesn't need to be searched
def min_value(node: Node):
    current = node

    # loop down to find the leftmost leaf
    while current:
        if current.left is None:
            break
        current = current.left

    return current


def inorder_successor(root: Node, n: Node):
    if n.right is not None:
        return min_value(n.right)

    successor = Node(None)

    while root:
        if root.data < n.data:
            root = root.right
        elif root.data > n.data:
            successor = root
            root = root.left
        else:
            break

    return successor


# Driver program to test above function
if __name__ == "__main__":
    root = None

    # Creating the tree given in the above diagram
    root = insert(root, 20)
    root = insert(root, 8)
    root = insert(root, 22)
    root = insert(root, 4)
    root = insert(root, 12)
    root = insert(root, 10)
    root = insert(root, 14)
    temp = root.left.right

    succ = inorder_successor(root, temp)
    if succ is not None:
        print("Inorder Successor of ", temp.data, "is ", succ.data)
    else:
        print("InInorder Successor doesn't exist")
