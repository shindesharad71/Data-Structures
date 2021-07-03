# Construct a tree from Inorder and Level order traversals
# https://www.geeksforgeeks.org/construct-tree-inorder-level-order-traversals/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def print_inorder(root: Node):
    if root:
        print_inorder(root.left)
        print(root.data, end=" ")
        print_inorder(root.right)


def build_tree(level_order: list, inorder: list):
    """Recursive function to construct binary tree of size n from
    Inorder traversal ino[] and Level Order traversal level[].
    The function doesn't do any error checking for cases
    where inorder and level order do not form a tree"""

    # Check if inorder array in not empty
    if inorder:
        # check if that element is exists in the level order
        for i in range(0, len(level_order)):
            if level_order[i] in inorder:
                # Create new node with matched element
                # In the given level order array

                node = Node(level_order[i])

                # Get the index of the matched element
                # in level order array
                io_index = inorder.index(level_order[i])
                break

        # If inorder array is empty return node
        if not inorder:
            return node

        # Construct left and right subtree
        node.left = build_tree(level_order, inorder[0:io_index])
        node.right = build_tree(level_order, inorder[io_index + 1 : len(inorder)])
        return node


# Driver code
if __name__ == "__main__":
    level_order = [20, 8, 22, 4, 12, 10, 14]
    inorder = [4, 8, 10, 12, 14, 20, 22]

    ino_len = len(inorder)
    root = build_tree(level_order, inorder)

    # Let us test the build tree by
    # printing Inorder traversal
    print("Inorder traversal of the constructed tree is")
    print_inorder(root)
