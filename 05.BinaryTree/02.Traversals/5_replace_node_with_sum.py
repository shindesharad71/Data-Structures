# Replace each node in binary tree with the sum of its inorder predecessor and successor
# https://www.geeksforgeeks.org/replace-node-binary-tree-sum-inorder-predecessor-successor/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def store_inorder_traversal(root: Node, arr: list):
    if not root:
        return

    store_inorder_traversal(root.left, arr)
    arr.append(root.data)
    store_inorder_traversal(root.right, arr)


def replace_node_with_sum(root: Node, arr: list, i: int):
    if not root:
        return

    replace_node_with_sum(root.left, arr, i)

    root.data = arr[i[0] - 1] + arr[i[0] + 1]

    i[0] += 1

    replace_node_with_sum(root.right, arr, i)


def replace_node_with_sum_util(root: Node):
    if not root:
        return

    arr = []

    arr.append(0)

    store_inorder_traversal(root, arr)

    arr.append(0)

    i = [1]

    replace_node_with_sum(root, arr, i)


def preorder(root: Node):
    if not root:
        return

    print(root.data, end=" ")

    preorder(root.left)
    preorder(root.right)


# Driver Code
if __name__ == "__main__":
    # binary tree formation
    root = Node(1)  # 1
    root.left = Node(2)  # / \
    root.right = Node(3)  # 2     3
    root.left.left = Node(4)  # / \ / \
    root.left.right = Node(5)  # 4 5 6 7
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Preorder Traversal before tree modification:")
    preorder(root)

    replace_node_with_sum_util(root)
    print()
    print("Preorder Traversal after tree modification:")
    preorder(root)
