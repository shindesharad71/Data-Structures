# Remove all leaf nodes from the binary search tree
# https://www.geeksforgeeks.org/remove-leaf-nodes-binary-search-tree/


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = self.right = None
