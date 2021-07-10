# Print BST keys in the given range
# https://www.geeksforgeeks.org/print-bst-keys-in-the-given-range/

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# The function prints all the keys in the given range
# [k1..k2]. Assumes that k1 < k2
def print_keys_between_range(root: Node, k1: int, k2: int):
    if root is None:
        return

    # Since the desired o/p is sorted, recurse for left
    # subtree first. If root.data is greater than k1, then
    # only we can get o/p keys in left subtree
    if k1 < root.data:
        print_keys_between_range(root.left, k1, k2)

    # If root's data lies in range, then prints root's data
    if k1 <= root.data <= k2:
        print(root.data, end=" ")

    # If root.data is smaller than k2, then only we can get
    # o/p keys in right subtree
    if k2 > root.data:
        print_keys_between_range(root.right, k1, k2)


# Driver Program
if __name__ == "__main__":
    k1 = 10
    k2 = 25
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)

    print_keys_between_range(root, k1, k2)
