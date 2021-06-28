# Foldable Binary Trees
# https://www.geeksforgeeks.org/foldable-binary-trees/

# Question: Given a binary tree, find out if the tree can be folded or not.
# A tree can be folded if left and right subtrees of the tree are structure
# wise mirror image of each other.
# An empty tree is considered as foldable.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Returns true if the given tree can be folded
def is_foldable(root: Node) -> bool:
    if root is None:
        return True
    return is_foldable_util(root.left, root.right)


def is_foldable_util(n1: Node, n2: Node) -> bool:
    # If both left and right subtrees are null then return true
    if n1 is None and n2 is None:
        return True

    # If one of trees is null and other is not then return false
    if n1 is None or n2 is None:
        return False

    # Otherwise check if left and
    # right subtrees are mirrors of
    # their counterparts

    d1 = is_foldable_util(n1.left, n2.right)
    d2 = is_foldable_util(n1.right, n2.left)

    return d1 and d2


# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)

    if is_foldable(root):
        print("Tree is foldable")
    else:
        print("Tree is not foldable")
