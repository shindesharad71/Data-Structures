# Find a pair with given sum in a Balanced BST
# https://www.geeksforgeeks.org/find-a-pair-with-given-sum-in-bst/


class Node:
    # Construct to create a new Node
    def __init__(self, key):
        self.data = key
        self.left = self.right = None


# A utility function to insert a new
# Node with given key in BST
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


def tree_to_list(root: Node, arr: list):
    if not root:
        return arr

    tree_to_list(root.left, arr)
    arr.append(root.data)
    tree_to_list(root.right, arr)

    return arr


def find_pair_with_given_sum_bst(root: Node, target: int) -> bool:
    arr1 = []

    arr2 = tree_to_list(root, arr1)

    start = 0
    end = len(arr2) - 1

    while start < end:
        # If target found
        if arr2[start] + arr2[end] == target:
            print(f"Pair Found: {arr2[start]} + {arr2[end]} = {target}")
            return True

        if arr2[start] + arr2[end] > target:
            end -= 1

        if arr2[start] + arr2[end] < target:
            start += 1

    print("No such values are found!")
    return False


if __name__ == "__main__":
    root = None
    root = insert(root, 15)
    root = insert(root, 10)
    root = insert(root, 20)
    root = insert(root, 8)
    root = insert(root, 12)
    root = insert(root, 16)
    root = insert(root, 25)

    find_pair_with_given_sum_bst(root, 33)
