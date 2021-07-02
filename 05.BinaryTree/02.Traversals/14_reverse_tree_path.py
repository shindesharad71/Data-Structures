# Reverse tree path
# https://www.geeksforgeeks.org/reverse-tree-path/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def reverse_tree_path_util(root: Node, data, temp, level, next_pos):
    if root is None:
        return None, temp, next_pos

    if data == root.data:
        temp[level] = root.data

        root.data = temp[next_pos]

        next_pos += 1

        return root, temp, next_pos

    temp[level] = root.data

    right = None

    left, temp, next_pos = reverse_tree_path_util(
        root.left, data, temp, level + 1, next_pos
    )

    if left is None:
        right, temp, next_pos = reverse_tree_path_util(
            root.right, data, temp, level + 1, next_pos
        )

    if left or right:
        root.data = temp[next_pos]

        next_pos += 1

        return left if left is not None else right, temp, next_pos

    return None, temp, next_pos


def reverse_tree_path(root: Node, data):
    temp = dict()

    next_pos = 0

    reverse_tree_path_util(root, data, temp, 0, next_pos)


def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Driver code
if __name__ == "__main__":
    # Let us create binary tree shown in above diagram
    root = Node(7)
    root.left = Node(6)
    root.right = Node(5)
    root.left.left = Node(4)
    root.left.right = Node(3)
    root.right.left = Node(2)
    root.right.right = Node(1)

    """     7
         /    \
        6       5
       / \     / \
      4  3     2  1          """

    data = 4

    # Reverse Tree Path
    reverse_tree_path(root, data)

    # Traverse inorder
    inorder(root)
