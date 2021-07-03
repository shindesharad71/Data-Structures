# Construct Tree from given Inorder and Preorder traversals
# https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def search(array: list, start, end, value):
    for i in range(start, end + 1):
        if array[i] == value:
            return i


def print_inorder(root: Node):
    if root:
        print_inorder(root.left)
        print(root.data, end=" ")
        print_inorder(root.right)


def build_tree(inorder, preorder, in_start, in_end):
    """Recursive function to construct binary of size len from
    Inorder traversal in[] and Preorder traversal pre[].
    Initial values of inStrt and inEnd should be 0 and len -1.
    The function doesn't do any error checking for cases where inorder and preorder
    do not form a tree"""
    if in_start > in_end:
        return None

    # Pitch current node from Preorder traversal using
    # preIndex and increment preIndex
    node = Node(preorder[build_tree.pre_index])
    build_tree.pre_index += 1

    # If this node has no children then return
    if in_start == in_end:
        return node

    # else find end of this node in inorder traversal
    in_index = search(inorder, in_start, in_end, node.data)

    # Using index in Inorder Traversal, construct left
    # and right subtrees
    node.left = build_tree(inorder, preorder, in_start, in_index - 1)
    node.right = build_tree(inorder, preorder, in_index + 1, in_end)

    return node


# Driver program
if __name__ == "__main__":
    inorder = ["D", "B", "E", "A", "F", "C"]
    preorder = ["A", "B", "D", "E", "C", "F"]
    # Static variable preIndex
    build_tree.pre_index = 0
    root = build_tree(inorder, preorder, 0, len(inorder) - 1)

    # Let us test the build tree by printing Inorder traversal
    print("Inorder traversal of the constructed tree is ")
    print_inorder(root)
