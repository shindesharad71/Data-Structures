# Count BST nodes that lie in a given range
# https://www.geeksforgeeks.org/count-bst-nodes-that-are-in-a-given-range/

# Utility function to create new node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Returns count of nodes in BST in
# range [low, high]
def get_count(root: Node, low: int, high: int) -> int:
    if root is None:
        return 0

    # Special Optional case for improving
    # efficiency
    if root.data == high and root.data == low:
        return 1

    # If current node is in range, then
    # include it in count and recur for
    # left and right children of it
    if high >= root.data >= low:
        return 1 + get_count(root.left, low, high) + get_count(root.right, low, high)

    # If current node is smaller than low,
    # then recur for right child
    elif root.data < low:
        return get_count(root.right, low, high)

    else:
        return get_count(root.left, low, high)


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
    #     10
    #     / \
    # 5     50
    # /     / \
    # 1     40 100
    l = 5
    h = 45
    print("Count of nodes between [", l, ", ", h, "] is ", get_count(root, l, h))
