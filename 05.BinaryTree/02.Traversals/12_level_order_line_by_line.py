# Level order traversal line by line | Set 3 (Using One Queue)
# https://www.geeksforgeeks.org/level-order-traversal-line-line-set-3-using-one-queue/

from collections import deque as queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Function to do level order
# traversal line by line
def level_order_traversal(root: Node):
    if root is None:
        return

    # Create an empty queue for
    # level order traversal
    q = queue()

    # Enqueue Root and None node.
    q.append(root)
    q.append(None)

    while len(q) > 1:
        curr = q.popleft()

        # Condition to check
        # occurrence of next
        # level.
        if curr is None:
            q.append(None)
            print()

        else:
            # Pushing left child of
            # current node.
            if curr.left:
                q.append(curr.left)

            # Pushing right child of
            # current node.
            if curr.right:
                q.append(curr.right)

            print(curr.data, end=" ")


# Driver code
if __name__ == "__main__":
    # Let us create binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    level_order_traversal(root)
