# Construct BST from given preorder traversal
# https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/

# A O(n^2) Python3 program for
# construction of BST from preorder traversal

# A binary tree node


class Node:
    # A constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# construct_tree_util.preIndex is a static variable of
# function construct_tree_util

# Function to get the value of static variable
# construct_tree_util.preIndex
def get_pre_index():
    return construct_tree_util.pre_index


# Function to increment the value of static variable
# construct_tree_util.preIndex


def increment_pre_index():
    construct_tree_util.preIndex += 1


# A recurseive function to construct Full from pre[].
# preIndex is used to keep track of index in pre[[].


def construct_tree_util(pre, low, high):
    # Base Case
    if low > high:
        return None

    # The first node in preorder traversal is root. So take
    # the node at preIndex from pre[] and make it root,
    # and increment preIndex
    root = Node(pre[get_pre_index()])
    increment_pre_index()

    # If the current subarray has onlye one element,
    # no need to recur
    if low == high:
        return root

    r_root = -1

    # Search for the first element greater than root
    for i in range(low, high + 1):
        if pre[i] > root.data:
            r_root = i
            break

    # If no elements are greater than the current root,
    # all elements are left children
    # so assign root appropriately
    if r_root == -1:
        r_root = get_pre_index() + (high - low)

    # Use the index of element found in preorder to divide
    # preorder array in two parts. Left subtree and right
    # subtree
    root.left = construct_tree_util(pre, get_pre_index(), r_root - 1)

    root.right = construct_tree_util(pre, r_root, high)

    return root


# The main function to construct BST from given preorder
# traversal. This function mailny uses construct_tree_util()


def construct_tree(pre):
    size = len(pre)
    construct_tree_util.preIndex = 0
    return construct_tree_util(pre, 0, size - 1)


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# Driver Code
if __name__ == "__main__":
    pre = [10, 5, 1, 7, 40, 50]
    root = construct_tree(pre)

    print("Inorder traversal of constructed tree")
    inorder(root)
