# Find all possible binary trees with given Inorder Traversal
# https://www.geeksforgeeks.org/find-all-possible-trees-with-given-inorder-traversal/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# A utility function to do preorder traversal of BST
def preorder(root: Node):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


def get_trees(arr, start, end):
    # List to store all possible trees
    trees = []

    # if start > end then subtree will be empty so returning NULL in the list
    if start > end:
        trees.append(None)
        return trees

    #  Iterating through all values from start to end for constructing left and right subtree recursively
    for i in range(start, end + 1):

        # Constructing left subtree
        ltrees = get_trees(arr, start, i - 1)

        # Constructing right subtree
        rtrees = get_trees(arr, i + 1, end)

        # Looping through all left and right subtrees and connecting to ith root below
        for j in ltrees:
            for k in rtrees:
                # Making arr[i] as root
                node = Node(arr[i])

                # Connecting left subtree
                node.left = j

                # Connecting right subtree
                node.right = k

                # Adding this tree to list
                trees.append(node)

    return trees


# Driver Program
if __name__ == "__main__":

    inp = [4, 5, 7]
    n = len(inp)

    trees = get_trees(inp, 0, n - 1)

    print("Preorder traversals of different possible Binary Trees are")
    for i in trees:
        preorder(i)
        print()
