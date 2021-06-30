# Find n-th node in Postorder traversal of a Binary Tree
# https://www.geeksforgeeks.org/find-n-th-node-in-postorder-traversal-of-a-binary-tree/

count = 0


# A Binary Tree Node
# Utility function to create a
# new tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def nth_node_postorder(root: Node, n):
    """Given a binary tree, print the nth
    node of inorder traversal"""
    global count
    if root is None:
        return

    if count <= n:
        """first recur on left child"""
        nth_node_postorder(root.left, n)

        """ now recur on right child """
        nth_node_postorder(root.right, n)

        """Increment counter"""
        count += 1

        # when count = n then print element
        if count == n:
            print(root.data)


# Driver Code
if __name__ == "__main__":
    root = Node(25)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(18)
    root.left.right = Node(22)
    root.right.left = Node(24)
    root.right.right = Node(32)

    n = 6

    nth_node_postorder(root, n)
