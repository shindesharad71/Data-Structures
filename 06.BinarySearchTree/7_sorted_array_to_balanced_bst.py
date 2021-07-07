# Sorted Array to Balanced BST
# https://www.geeksforgeeks.org/sorted-array-to-balanced-bst/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def sorted_array_to_bst(arr: list):
    if not arr:
        return None

    mid = int(len(arr)) // 2

    root = Node(arr[mid])

    root.left = sorted_array_to_bst(arr[:mid])

    root.right = sorted_array_to_bst(arr[mid + 1 :])
    return root


def preorder(root: Node):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Driver Program
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = sorted_array_to_bst(arr)
    print("PreOrder Traversal of constructed BST")
    preorder(root)
