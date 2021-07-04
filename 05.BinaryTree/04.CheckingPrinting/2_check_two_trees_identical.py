# Write Code to Determine if Two Trees are Identical
# https://www.geeksforgeeks.org/write-c-code-to-determine-if-two-trees-are-identical/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def identical_trees(a: Node, b: Node) -> bool:
    if a is None and b is None:
        return True

    if a is not None and b is not None:
        return identical_trees(a.left, b.left) and identical_trees(a.right, b.right)

    return False


# Driver Program
if __name__ == "__main__":
    root1 = Node(1)
    root2 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)

    if identical_trees(root1, root2):
        print("Both trees are identical")
    else:
        print("Trees are not identical")
