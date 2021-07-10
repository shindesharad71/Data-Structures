# Simple Recursive solution to check whether BST contains dead end
# https://www.geeksforgeeks.org/simple-recursive-solution-check-whether-bst-contains-dead-end/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# A utility function to insert a
# new Node with given key in BST
def insert(root: Node, data):
    # If the tree is empty,
    # return a new Node
    if root is None:
        return Node(data)

    # Otherwise, recur down the tree
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    # return the (unchanged) Node pointer
    return root


# Returns true if tree with given
# root contains dead end or not.
# min and max indicate range
# of allowed values for current node.
# Initially these values are full range.
def dead_end(root: Node, min, max):
    # if the root is null or the recursion
    # moves after leaf node it will return
    # false i.e no dead end.
    if root is None:
        return False

    # if this occurs means dead
    # end is present.
    if min == max:
        return True

    # Recursion
    return dead_end(root.left, min, root.data - 1) or dead_end(
        root.right, root.data + 1, max
    )


# Driver Code
if __name__ == "__main__":

    #         8
    #     / \
    #     5 11
    #     / \
    # 2 7
    #     \
    #     3
    #     \
    #     4
    root = None
    root = insert(root, 8)
    root = insert(root, 5)
    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 7)
    root = insert(root, 11)
    root = insert(root, 4)
    if dead_end(root, 1, 9999999999):
        print("Yes")
    else:
        print("No")
