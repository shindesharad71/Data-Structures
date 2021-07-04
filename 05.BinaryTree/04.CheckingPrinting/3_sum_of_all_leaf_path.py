# Sum of all the numbers that are formed from root to leaf paths
# https://www.geeksforgeeks.org/sum-numbers-formed-root-leaf-paths/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Returns sums of all root to leaf paths. The first parameter is root
# of current subtree, the second parameter is value of the number
# formed by nodes from root to this node
def tree_path_sum_util(root: Node, val):
    if root is None:
        return 0

    val = val * 10 + root.data

    # If current node is leaf, return the current value of val
    if root.left is None and root.right is None:
        return val

    return tree_path_sum_util(root.left, val) + tree_path_sum_util(root.right, val)


# A wrapper function over treePathSumUtil()
def tree_paths_sum(root):
    # Pass the initial value as 0 as there is nothing above root
    return tree_path_sum_util(root, 0)


# Driver function to test above function
if __name__ == "__main__":
    root = Node(6)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(5)
    root.right.right = Node(4)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)
    print("Sum of all paths is ", tree_paths_sum(root))
