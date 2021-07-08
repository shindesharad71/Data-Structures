# Binary Search Tree Implementation
# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

# Individual node in BST
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Insert New Node
def insert(root: Node, data) -> Node:
    if root is None:
        return Node(data)

    if root.data == data:
        return root
    elif root.data < data:
        root.right = insert(root.right, data)
    else:
        root.left = insert(root.left, data)

    return root


# Search in BST
def search(root: Node, key):
    if root is None or root.data == key:
        return root

    if root.data > key:
        return search(root.right, key)

    return search(root.left, key)


# Inorder tree traversal
def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


if __name__ == "__main__":
    # Driver program to test the above functions
    # Let us create the following BST
    #    50
    #  /     \
    # 30     70
    #  / \ / \
    # 20 40 60 80

    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)

    # Print inorder traversal of the BST
    inorder(r)
