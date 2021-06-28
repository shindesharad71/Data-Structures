# Expression Tree
# https://www.geeksforgeeks.org/expression-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def is_operator(char: str) -> bool:
    if char == "+" or char == "-" or char == "*" or char == "/" or char == "^":
        return True
    return False


def inorder(t: Node):
    if t is not None:
        inorder(t.left)
        print(t.data)
        inorder(t.right)


def construct_tree(postfix) -> str:
    stack = []
