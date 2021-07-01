# Level Order Binary Tree Traversal
# https://www.geeksforgeeks.org/level-order-tree-traversal/

# A node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def height(node: Node) -> int:
    """Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
    """
    if node is None:
        return 0

    # Compute the height of each subtree
    lheight = height(node.left)
    rheight = height(node.right)

    # Use the larger one
    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1


# Print nodes at a current level
def print_current_level(root: Node, level: int):
    if root is None:
        return

    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        print_current_level(root.left, level - 1)
        print_current_level(root.right, level - 1)


# Function to  print level order traversal of tree
def print_level_order(root: Node):
    h = height(root)

    for i in range(1, h + 1):
        print_current_level(root, i)


# Driver program to test above function
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Level order traversal of binary tree is -")
    print_level_order(root)
