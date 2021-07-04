# Vertical Sum in a given Binary Tree
# https://www.geeksforgeeks.org/vertical-sum-in-a-given-binary-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Traverses the tree in in-order form and
# populates a hashMap that contains the
# vertical sum
def vertical_sum_util(root: Node, hd: int, map: dict):
    if root is None:
        return

    vertical_sum_util(root.left, hd - 1, map)

    if hd in map.keys():
        map[hd] = map[hd] + root.data
    else:
        map[hd] = root.data

    vertical_sum_util(root.right, hd + 1, map)


def vertical_sum(root: Node):
    # a dictionary to store sum of
    # nodes for each horizontal distance
    map = {}

    # Populate the dictionary
    vertical_sum_util(root, 0, map)

    # Prints the values stored
    # by VerticalSumUtil()
    for i, j in map.items():
        print(i, "=", j, end=", ")


# Driver Code
if __name__ == "__main__":
    """      Create the following Binary Tree
              1
            /    \
          2        3
         / \      / \
        4   5    6   7 
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(
        "Following are the values of vertical "
        "sums with the positions of the "
        "columns with respect to root"
    )

    print(vertical_sum(root))
