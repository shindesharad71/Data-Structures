# Print a Binary Tree in Vertical Order (Map based Method)
# https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/


class Node:
    def __init__(self, data):
        self.key = data
        self.left = self.right = None


def get_vertical_order(root: Node, hd, m: dict):
    if root is None:
        return

    try:
        m[hd].append(root.key)
    except:
        m[hd] = [root.key]

    # Store nodes in left subtree
    get_vertical_order(root.left, hd - 1, m)

    # Store nodes in right subtree
    get_vertical_order(root.right, hd + 1, m)


# The main function to print vertical order of a binary
# tree ith given root
def print_vertical_order(root: Node):
    # Create a map and store vertical order in map using
    # function get_vertical_order()
    m = dict()
    hd = 0
    get_vertical_order(root, hd, m)

    # Traverse the map and print nodes at every horizontal
    # distance (hd)
    for index, value in enumerate(sorted(m)):
        for i in m[value]:
            print(i, end=" ")
        print()


# Driver program to test above function
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)
    print("Vertical order traversal is")
    print_vertical_order(root)
