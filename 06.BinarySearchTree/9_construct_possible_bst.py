# Construct all possible BSTs for keys 1 to N
# https://www.geeksforgeeks.org/construct-all-possible-bsts-for-keys-1-to-n/

# How many structurally unique BSTs for keys from 1..N?


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def preorder(root: Node):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def construct_tree(start, end):
    arr = []

    """ if start > end then subtree will be
        empty so returning None in the list
    """
    if start > end:
        arr.append(None)
        return arr

    """ iterating through all values from
        start to end for constructing
        left and right subtree recursively
    """
    for i in range(start, end + 1):
        """constructing left subtree"""
        left_subtree = construct_tree(start, i - 1)

        """ constructing right subtree """
        right_subtree = construct_tree(i + 1, end)

        """ now looping through all left and
            right subtrees and connecting
            them to ith root below
        """
        for j in range(len(left_subtree)):
            left = left_subtree[j]
            for k in range(len(right_subtree)):
                right = right_subtree[k]
                node = Node(i)
                node.left = left
                node.right = right
                arr.append(node)

    return arr


# Driver Code
if __name__ == "__main__":
    # Construct all possible BSTs
    totalTreesFrom1toN = construct_tree(1, 3)

    """ Printing preorder traversal of
        all constructed BSTs """
    print("Preorder traversals of all constructed BSTs are")
    for i in range(len(totalTreesFrom1toN)):
        preorder(totalTreesFrom1toN[i])
        print()
