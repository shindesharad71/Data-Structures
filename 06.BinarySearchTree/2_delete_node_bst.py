# Delete node in BST
# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def insert(root: Node, data) -> Node:
    if root is None:
        return Node(data)

    if root.data < data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


# Given a non-empty binary
# search tree, return the node
# with minimum key value
# found in that tree. Note that the
# entire tree does not need to be searched
def min_value_node(root: Node):
    current = root

    # loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current


# Given a binary search tree and a key, this function
# delete the key and returns the new root
def delete_node(root: Node, key):
    if root is None:
        return root

    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.data:
        root.left = delete_node(root.left, key)

    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif key > root.data:
        root.right = delete_node(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = min_value_node(root.right)

        # Copy the inorder successor's
        # content to this node
        root.data = temp.data

        # Delete the inorder successor
        root.right = delete_node(root.right, temp.data)

    return root


# Driver code
if __name__ == "__main__":
    """ Let us create following BST
                  50
               /     \
              30      70
             /  \    /  \
           20   40  60   80 """

    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    print("Inorder traversal of the given tree")
    inorder(root)

    print("\nDelete 20")
    root = delete_node(root, 20)

    print("Inorder traversal of the modified tree")
    inorder(root)

    print("\nDelete 30")
    root = delete_node(root, 30)

    print("Inorder traversal of the modified tree")
    inorder(root)

    print("\nDelete 50")
    root = delete_node(root, 50)

    print("Inorder traversal of the modified tree")
    inorder(root)
