# Level Order Binary Tree Traversal
# https://www.geeksforgeeks.org/level-order-tree-traversal/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def height(node: Node) -> int:
    if node is None:
        return 0

    lheight = height(node.left)
    rheight = height(node.right)

    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1


def print_current_level(root: Node, level: int):
    if root is None:
        return

    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        print_current_level(root.left, level - 1)
        print_current_level(root.right, level - 1)


def print_level_order(root: Node):
    h = height(root)

    for i in range(1, h + 1):
        print_current_level(root, i)


# Driver program to test above function
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Level order traversal of binary tree is -")
    print_level_order(root)
