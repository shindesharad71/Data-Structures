# Construct BST from given preorder traversal
# https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/

INT_MIN = float("-infinity")
INT_MAX = float("infinity")


class Node:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None


def get_pre_index():
    return constuct_tree_util.pre_index


def increment_pre_index():
    construct_tree_util.pre_index += 1


def construct_tree_util(pre, key, min, max, size):
    if get_pre_index() >= size:
        return None
