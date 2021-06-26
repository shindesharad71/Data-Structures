# Binary Tree
# https://www.geeksforgeeks.org/binary-tree-set-1-introduction/

# A Python class that represents an individual node
# in a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
