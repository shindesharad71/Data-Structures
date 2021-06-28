# Tree Traversals (Inorder, Preorder and Postorder)
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Inorder traversal
def inorder(root: Node):
    if root:
        inorder(root.left)  # Left Child
        print(root.data)  # Print Data of Node
        inorder(root.right)  # Right Child


# Preorder traversal
def preorder(root: Node):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


# Postorder traversal
def postorder(root: Node):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


# Driver code
if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Preorder traversal of binary tree is")
    preorder(root)

    print("\nInorder traversal of binary tree is")
    inorder(root)

    print("\nPostorder traversal of binary tree is")
    postorder(root)
