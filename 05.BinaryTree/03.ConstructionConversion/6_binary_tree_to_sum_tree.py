# Convert a given tree to its Sum Tree
# https://www.geeksforgeeks.org/convert-a-given-tree-to-sum-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def to_sum_tree(root: Node):
    if root is None:
        return 0

    # Store old value
    old_val = root.data

    # Recursively call for left and
    # right subtrees and store the sum as
    # new value of this node
    root.data = to_sum_tree(root.left) + to_sum_tree(root.right)

    # Return the sum of values of nodes
    # in left and right subtrees and
    # old_value of this node
    return root.data + old_val


# A utility function to print
# inorder traversal of a Binary Tree
def print_inorder(root: Node):
    if root:
        print_inorder(root.left)
        print(root.data, end=" ")
        print_inorder(root.right)


# Driver Code
if __name__ == "__main__":
    root = None
    x = 0

    # Constructing tree given in the above figure
    root = Node(10)
    root.left = Node(-2)
    root.right = Node(6)
    root.left.left = Node(8)
    root.left.right = Node(-4)
    root.right.left = Node(7)
    root.right.right = Node(5)

    to_sum_tree(root)

    # Print inorder traversal of the converted
    # tree to test result of toSumTree()
    print("Inorder Traversal of the resultant tree is: ")
    print_inorder(root)
