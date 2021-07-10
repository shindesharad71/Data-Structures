# Largest number in BST which is less than or equal to N
# https://www.geeksforgeeks.org/largest-number-bst-less-equal-n/


class Node:

    # To create new BST Node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# To insert a new node in BST
def insert(root: Node, data):
    # If tree is empty return new node
    if root is None:
        return Node(data)

    # If key is less then or greater then
    # node value then recur down the tree
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    # Return the (unchanged) node pointer
    return root


# function to find max value less then N
def find_max_for_n(root: Node, N: int) -> int:
    # Base cases
    if root is None:
        return -1

    if root.data == N:
        return root.data

    # If root's value is smaller, try in
    # right subtree
    elif root.data < N:
        k = find_max_for_n(root.right, N)
        if k == -1:
            return root.data
        else:
            return k

    # If root's key is greater, return
    # value from left subtree.
    elif root.data > N:
        return find_max_for_n(root.left, N)


# Driver code
if __name__ == "__main__":
    N = 4

    # creating following BST
    #
    #             5
    #         / \
    #         2     12
    #     / \ / \
    #     1 3 9 21
    #                 / \
    #             19 25
    root = None
    root = insert(root, 25)
    insert(root, 2)
    insert(root, 1)
    insert(root, 3)
    insert(root, 12)
    insert(root, 9)
    insert(root, 21)
    insert(root, 19)
    insert(root, 25)
    print(find_max_for_n(root, N))
