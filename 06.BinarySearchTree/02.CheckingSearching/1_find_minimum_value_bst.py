# Find the node with minimum value in a Binary Search Tree
# https://www.geeksforgeeks.org/find-the-minimum-element-in-a-binary-search-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def insert(node, data):
    # 1. If the tree is empty, return a new,
    # single node
    if node is None:
        return Node(data)

    else:
        # 2. Otherwise, recur down the tree
        if data <= node.data:
            node.left = insert(node.left, data)
        else:
            node.right = insert(node.right, data)

        # Return the (unchanged) node pointer
        return node


def find_minimum_node(root: Node):
    current = root

    while current.left is not None:
        current = current.left

    return current.data


# Driver Code
if __name__ == "__main__":
    root = None
    root = insert(root, 4)
    insert(root, 2)
    insert(root, 1)
    insert(root, 3)
    insert(root, 6)
    insert(root, 5)

    print("Minimum value in BST is: ", find_minimum_node(root))
