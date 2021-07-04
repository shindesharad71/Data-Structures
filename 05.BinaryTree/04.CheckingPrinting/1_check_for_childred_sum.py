# Check for Children Sum Property in a Binary Tree
# https://www.geeksforgeeks.org/check-for-children-sum-property-in-a-binary-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def is_sum_property(root: Node):
    left_data = 0
    right_data = 0

    if root is None or (root.left is None and root.right is None):
        return 1

    else:
        if root.left is not None:
            left_data = root.left.data

        if root.right is not None:
            right_data = root.right.data

        if (
            (root.data == left_data + right_data)
            and is_sum_property(root.left)
            and is_sum_property(root.right)
        ):
            return 1
        else:
            return 0


# Driver Code
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.right = Node(2)
    if is_sum_property(root):
        print("The given tree satisfies the children sum property")
    else:
        print("The given tree does not satisfy the children sum property")
