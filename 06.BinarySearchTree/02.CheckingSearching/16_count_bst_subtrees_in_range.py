# Count BST subtrees that lie in given range
# https://www.geeksforgeeks.org/count-bst-subtrees-that-lie-in-given-range/

# Utility function to create new node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# A utility function to check if data of
# root is in range from low to high
def in_range(root, low, high):
    return low <= root.data <= high


# A recursive function to get count of nodes
# whose subtree is in range from low to high.
# This function returns true if nodes in subtree
# rooted under 'root' are in range.
def get_count_util(root: Node, low: int, high: int, count):
    if root is None:
        return True

    # Recur for left and right subtrees
    l = get_count_util(root.left, low, high, count)
    r = get_count_util(root.right, low, high, count)

    # If both left and right subtrees are in range
    # and current node is also in range, then
    # increment count and return true
    if l and r and in_range(root, low, high):
        count[0] += 1
        return True

    return False


# A wrapper over get_count_util(). This function
# initializes count as 0 and calls get_count_util()
def get_count(root: Node, low: int, high: int):
    count = [0]
    get_count_util(root, low, high, count)
    return count


# Driver Code
if __name__ == "__main__":
    # Let us construct the BST
    root = Node(10)
    root.left = Node(5)
    root.right = Node(50)
    root.left.left = Node(1)
    root.right.left = Node(40)
    root.right.right = Node(100)

    # Let us constructed BST shown in above example
    # 10
    # / \
    # 5     50
    # /     / \
    # 1     40 100
    l = 5
    h = 45
    print("Count of subtrees in [", l, ", ", h, "] is ", get_count(root, l, h))
