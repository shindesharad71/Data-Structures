# Construct a special tree from given preorder traversal
# https://www.geeksforgeeks.org/construct-a-special-tree-from-given-preorder-traversal/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def print_inorder(root: Node):
    if root:
        print_inorder(root.left)
        print(root.data, end=" ")
        print_inorder(root.right)


# A recursive function to create a
# Binary Tree from given pre[] preLN[]
# arrays. The function returns root of
# tree. index_ptr is used to update
# index values in recursive calls. index
# must be initially passed as 0
def construct_tree_util(pre: list, preLN: list, index_ptr, n: int):
    index = index_ptr[0]

    # Base case
    if index == n:
        return None

    # Allocate memory for this node and
    # increment index for subsequent
    # recursive calls
    temp = Node(pre[index])
    index_ptr[0] += 1

    # If this is an internal node, construct left
    # and right subtrees and link the subtrees
    if preLN[index] == "N":
        temp.left = construct_tree_util(pre, preLN, index_ptr, n)
        temp.right = construct_tree_util(pre, preLN, index_ptr, n)

    return temp


# A wrapper over constructTreeUtil()
def construct_tree(pre: list, preLN: list, n: int):
    index = [0]
    return construct_tree_util(pre, preLN, index, n)


if __name__ == "__main__":
    root = None

    pre = [10, 30, 20, 5, 15]
    preLN = ["N", "N", "L", "L", "L"]
    n = len(pre)

    # construct the above tree
    root = construct_tree(pre, preLN, n)

    # Test the constructed tree
    print("Following is Inorder Traversal of the Constructed Binary Tree:")
    print_inorder(root)
