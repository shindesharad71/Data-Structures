# Remove all leaf nodes from the binary search tree
# https://www.geeksforgeeks.org/remove-leaf-nodes-binary-search-tree/


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = self.right = None


def insert(root: Node, data: int) -> Node:
    if root is None:
        return Node(data)
    elif data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def delete_leaf_node(root: Node):
    if root is None:
        return None

    if root.left is None and root.right is None:
        return None

    # Else recursively delete in left
    # and right subtrees.
    root.left = delete_leaf_node(root.left)
    root.right = delete_leaf_node(root.right)

    return root


# Driver code
if __name__ == "__main__":
    root = None
    root = insert(root, 20)
    insert(root, 10)
    insert(root, 5)
    insert(root, 15)
    insert(root, 30)
    insert(root, 25)
    insert(root, 35)
    print("Inorder before Deleting the leaf Node.")
    inorder(root)
    delete_leaf_node(root)
    print()
    print("Inorder after Deleting the leaf Node.")
    inorder(root)
