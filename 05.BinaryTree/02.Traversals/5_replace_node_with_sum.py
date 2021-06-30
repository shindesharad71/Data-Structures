# Replace each node in binary tree with the sum of its inorder predecessor and successor
# https://www.geeksforgeeks.org/replace-node-binary-tree-sum-inorder-predecessor-successor/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def store_inorder_traversal(root: Node, arr: list):
    if not root:
        return

    store_inorder_traversal(root.left)
    arr.append(root.data)
    store_inorder_traversal(root.right)


def replace_node_with_sum(root: Node, arr: list, i: int):
    if not root:
        return

    replace_node_with_sum(root.left, arr, i)

    root.data = arr[i[0] - 1] + arr[i[0] + 1]
