# Reverse Level Order Traversal
# https://www.geeksforgeeks.org/reverse-level-order-traversal/

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def reverse_level_order(root: Node):
    q = deque()

    q.append(root)

    ans = deque()

    while q:
        node = q.popleft()

        ans.appendleft(node.data)

        if node.right:
            q.append(node.right)

        if node.left:
            q.append(node.left)

    return ans


# Driver Program
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Level Order traversal of binary tree is ", reverse_level_order(root))
