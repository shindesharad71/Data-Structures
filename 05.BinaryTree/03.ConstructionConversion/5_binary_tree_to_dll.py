# Convert a given Binary Tree to Doubly Linked List
# https://www.geeksforgeeks.org/in-place-convert-a-given-binary-tree-to-doubly-linked-list/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def btt_to_dll_util(root: Node):
    """This is a utility function to
    convert the binary tree to doubly
    linked list. Most of the core task
    is done by this function."""
    if root is None:
        return root

    # Convert the left subtree
    if root.left:
        left = btt_to_dll_util(root.left)

        # Find inorder predecessor, After
        # this loop, left will point to the
        # inorder predecessor of root
        while left.right:
            left = left.right

        # Make root as next of predecessor
        left.right = root

        # Make predecessor as
        # previous of root
        root.left = left

    # Convert the right subtree
    # and link to root
    if root.right:
        # Convert the right subtree
        right = btt_to_dll_util(root.right)

        # Find inorder successor, After
        # this loop, right will point to
        # the inorder successor of root
        while right.left:
            right = right.left

        # Make root as previous
        # of successor
        right.left = root

        # Make successor as
        # next of root
        root.right = right

    return root


def btt_to_dll(root: Node):
    # Convert to doubly linked
    # list using BLLToDLLUtil
    root = btt_to_dll_util(root)

    # We need pointer to left most
    # node which is head of the
    # constructed Doubly Linked list
    while root.left:
        root = root.left

    return root


def print_list(head):
    """Function to print the given
    doubly linked list"""
    if head is None:
        return
    while head:
        print(head.data, end=" ")
        head = head.right


# Driver Code
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    head = btt_to_dll(root)
    print_list(head)
