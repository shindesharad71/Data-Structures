# Two nodes of a BST are swapped, correct the BST
# https://www.geeksforgeeks.org/fix-two-swapped-nodes-of-bst/


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = self.right = None


def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def correct_bst_util(root: Node, first, middle, last, prev):
    if root:
        # Recur for the left sub tree
        correct_bst_util(root.left, first, middle, last, prev)

        # If this is the first violation, mark these
        # two nodes as 'first and 'middle'
        if prev[0] and root.data < prev[0].data:
            if not first[0]:
                first[0] = prev[0]
                middle[0] = root
            else:

                # If this is the second violation,
                # mark this node as last
                last[0] = root

        prev[0] = root

        # Recur for the right subtree
        correct_bst_util(root.right, first, middle, last, prev)


def correct_bst(root: Node):
    # Followed four lines just for forming
    # an array with only index 0 filled
    # with None and we will update it accordingly.
    # we made it null so that we can fill
    # node data in them.
    first = [None]
    middle = [None]
    last = [None]
    prev = [None]

    # Setting arrays (having zero index only)
    # for capturing the required node
    correct_bst_util(root, first, middle, last, prev)

    # Fixing the two nodes
    if first[0] and last[0]:

        # Swapping for first and last key values
        first[0].data, last[0].data = (last[0].data, first[0].data)

    elif first[0] and middle[0]:

        # Swapping for first and middle key values
        first[0].data, middle[0].data = (middle[0].data, first[0].data)


# Driver Code
if __name__ == "__main__":
    # Following 7 lines are for tree formation
    root = Node(6)
    root.left = Node(10)
    root.right = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(7)
    root.right.right = Node(12)

    # Printing inorder traversal of normal tree
    print("inorder traversal of normal tree")
    inorder(root)
    print("")

    # Function call to do the task
    correct_bst(root)

    # Printing inorder for corrected Bst tree
    print("")
    print("inorder for corrected BST")

    inorder(root)
