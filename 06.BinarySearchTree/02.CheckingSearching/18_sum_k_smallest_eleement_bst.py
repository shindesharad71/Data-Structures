# Sum of k smallest elements in BST
# https://www.geeksforgeeks.org/sum-k-smallest-elements-bst/

INT_MAX = 2147483647


class Node:
    # Construct to create a new Node
    def __init__(self, key):
        self.data = key
        self.left = self.right = None


# A utility function to insert a new
# Node with given key in BST and also
# maintain count ,Sum
def insert(root: Node, key: int):
    # If the tree is empty, return a new Node
    if root is None:
        return Node(key)

    # Otherwise, recur down the tree
    if root.data > key:
        root.left = insert(root.left, key)

    elif root.data < key:
        root.right = insert(root.right, key)

    # return the (unchanged) Node pointer
    return root


def kth_smallest_element_sum_util(root: Node, k: list, count: list):
    if root is None:
        return 0

    if count[0] > k[0]:
        return 0

    # Compute sum of elements in left subtree
    res = kth_smallest_element_sum_util(root.left, k, count)

    if count[0] >= k[0]:
        return res

    # Add root data
    res += root.data

    # Add current node
    count[0] += 1
    if count[0] >= k[0]:
        return res

    # If count is less than k, return
    # right subtree Nodes
    return res + kth_smallest_element_sum_util(root.right, k, count)


def kth_smallest_element_sum(root: Node, k):
    count = [0]
    return kth_smallest_element_sum_util(root, k, count)


# Driver Code
if __name__ == "__main__":
    """ 20
        / \
    8 22
    / \
    4 12
        / \
        10 14
        """
    root = None
    root = insert(root, 20)
    root = insert(root, 8)
    root = insert(root, 4)
    root = insert(root, 12)
    root = insert(root, 10)
    root = insert(root, 14)
    root = insert(root, 22)

    k = [3]
    print(kth_smallest_element_sum(root, k))
