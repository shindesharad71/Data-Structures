# K’th Largest Element in BST when modification to BST is not allowed
# https://www.geeksforgeeks.org/kth-largest-element-in-bst-when-modification-to-bst-is-not-allowed/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# A function to find k'th largest
# element in a given tree.
def kth_largest_util(root: Node, k, c):
    # Base cases, the second condition
    # is important to avoid unnecessary
    # recursive calls
    if root is None or c[0] >= k:
        return

    # Follow reverse inorder traversal
    # so that the largest element is
    # visited first
    kth_largest_util(root.right, k, c)

    # Increment the visited nodes
    c[0] += 1

    # If c becomes k now, then this is
    # the k'th largest
    if c[0] == k:
        print("K'th largest element is ", root.data)
        return

    # Recur left subtree
    kth_largest_util(root.left, k, c)


# Function to find k'th largest element
def kth_largest(root: Node, k):
    # Initialize count of nodes visited as 0
    c = [0]

    # Note that c is passed by reference
    kth_largest_util(root, k, c)


# A utility function to insert a new
# node with given key in BST
def insert(root: Node, data):
    # If the tree is empty,
    # return a new node
    if root is None:
        return Node(data)

    # Otherwise, recur down the tree
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    # return the (unchanged) node pointer
    return root


# Driver Code
if __name__ == "__main__":

    # Let us create following BST
    #         50
    #     /     \
    #     30     70
    # / \ / \
    # 20 40 60 80 */
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    for k in range(1, 8):
        kth_largest(root, k)
