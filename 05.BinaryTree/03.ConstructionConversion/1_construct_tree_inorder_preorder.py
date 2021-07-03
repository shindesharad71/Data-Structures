# Construct Tree from given Inorder and Preorder traversals
# https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


"""Recursive function to construct binary of size len from
   Inorder traversal in[] and Preorder traversal pre[].
   Initial values of inStrt and inEnd should be 0 and len -1.
   The function doesn't do any error checking for cases where inorder and preorder 
   do not form a tree"""


def build_tree(inorder, preorder, in_start, in_end):
    if in_start > in_end:
        return None

    # Pitch current node from Preorder traversal using
    # preIndex and increment preIndex
    node = Node(preorder[build_tree.pre_index])
    build_tree.pre_index += 1

    # If this node has no children then return
    if in_start == in_end:
        return node
