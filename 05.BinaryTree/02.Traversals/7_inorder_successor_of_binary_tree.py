# Inorder Successor of a node in Binary Tree
# https://www.geeksforgeeks.org/inorder-succesor-node-binary-tree/

# global variable
next = None


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# function that prints the inorder successor
# of a target node. next will point the last
# tracked node, which will be the answer.
def inorder_successor(root: Node, target_node: Node):
    global next

    # if root is None then return
    if root is None:
        return

    inorder_successor(root.right, target_node)

    if root.data == target_node.data:
        # this will be true to the last node
        # in inorder traversal i.e., rightmost node.
        if next is None:
            print("inorder successor of ", root.data, "is: None")

        else:
            print("inorder successor of ", root.data, "is: ", next.data)

    next = root

    inorder_successor(root.left, target_node)


# Driver Code
if __name__ == "__main__":
    # Let's construct the binary tree
    # as shown in above diagram.
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    # Case 1
    next = None
    inorder_successor(root, root.right)

    # case 2
    next = None
    inorder_successor(root, root.left.left)

    # case 3
    next = None
    inorder_successor(root, root.right.right)
