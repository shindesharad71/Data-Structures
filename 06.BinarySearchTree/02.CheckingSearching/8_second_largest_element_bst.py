# Second largest element in BST
# https://www.geeksforgeeks.org/second-largest-element-in-binary-search-tree-bst/


class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def second_largest_util(root: Node, c):
    # Base cases, the second condition
    # is important to avoid unnecessary
    # recursive calls
    if root is None or c[0] >= 2:
        return

    # Follow reverse inorder traversal so that
    # the largest element is visited first
    second_largest_util(root.right, c)

    c[0] += 1

    # If c becomes k now, then this is
    # the 2nd largest
    if c[0] == 2:
        print("2nd largest element is", root.data)
        return

    # Recur for left subtree
    second_largest_util(root.left, c)


# Function to find 2nd largest element
def second_largest(root):
    # Initialize count of nodes visited as 0
    c = [0]

    # Note that c is passed by reference
    second_largest_util(root, c)


# A utility function to insert a new
# node with given key in BST
def insert(node: Node, data):
    # If the tree is empty, return a new node
    if node is None:
        return Node(data)

    # Otherwise, recur down the tree
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)

    # return the (unchanged) node pointer
    return node


# Driver Code
if __name__ == "__main__":
    # Let us create following BST
    #         50
    #     /     \
    #     30     70
    #     / \ / \
    # 20 40 60 80
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    second_largest(root)
