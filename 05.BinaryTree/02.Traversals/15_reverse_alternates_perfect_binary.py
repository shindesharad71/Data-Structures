# Reverse alternate levels of a perfect binary tree
# https://www.geeksforgeeks.org/reverse-alternate-levels-binary-tree/

MAX = 100


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# A utility function to
# reverse an array from
# index 0 to n-1
def reverse(arr, n):
    l = 0
    r = n - 1

    while l < r:
        arr[l], arr[r] = (arr[r], arr[l])
        l += 1
        r -= 1


# Function to store nodes of
# alternate levels in an array
def store_alternate(root: Node, arr, index, l):
    if root is None:
        return index

    # Store elements of
    # left subtree
    index = store_alternate(root.left, arr, index, l + 1)

    # Store this node only if
    # this is a odd level node
    if l % 2 != 0:
        arr[index] = root.data
        index += 1

    # Store elements of right
    # subtree
    index = store_alternate(root.right, arr, index, l + 1)

    return index


def modify_tree(root, arr, index, l):
    if root is None:
        return index

    # Update nodes in left subtree
    index = modify_tree(root.left, arr, index, l + 1)

    # Update this node only
    # if this is an odd level node
    if l % 2 != 0:
        root.data = arr[index]
        index += 1

    # Update nodes in right subtree
    index = modify_tree(root.right, arr, index, l + 1)

    return index


def reverse_alternate(root: Node):
    arr = [0] * MAX
    index = 0

    index = store_alternate(root, arr, index, 0)

    reverse(arr, index)

    index = 0
    index = modify_tree(root, arr, index, 0)


# A utility function to print
# indorder traversal of a
# binary tree
def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.data, end=" ")
        print_inorder(root.right)


# Driver code
if __name__ == "__main__":
    root = Node("a")
    root.left = Node("b")
    root.right = Node("c")
    root.left.left = Node("d")
    root.left.right = Node("e")
    root.right.left = Node("f")
    root.right.right = Node("g")
    root.left.left.left = Node("h")
    root.left.left.right = Node("i")
    root.left.right.left = Node("j")
    root.left.right.right = Node("k")
    root.right.left.left = Node("l")
    root.right.left.right = Node("m")
    root.right.right.left = Node("n")
    root.right.right.right = Node("o")

    print("Inorder Traversal of given tree")
    print_inorder(root)

    reverse_alternate(root)

    print("\nInorder Traversal of modified tree")
    print_inorder(root)
