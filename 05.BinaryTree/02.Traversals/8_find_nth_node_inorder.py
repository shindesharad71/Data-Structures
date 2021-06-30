# Find n-th node of inorder traversal
# https://www.geeksforgeeks.org/find-n-th-node-inorder-traversal/

count = 0


# A Binary Tree Node
# Utility function to create a
# new tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def nth_node_inorder(root: Node, n):
    """Given a binary tree, print the nth
    node of inorder traversal"""
    global count
    if root is None:
        return

    if count <= n:
        """first recur on left child"""
        nth_node_inorder(root.left, n)
        count += 1

        # when count = n then print element
        if count == n:
            print(root.data, end=" ")

        """ now recur on right child """
        nth_node_inorder(root.right, n)


# Driver Code
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)

    n = 4

    nth_node_inorder(root, n)
