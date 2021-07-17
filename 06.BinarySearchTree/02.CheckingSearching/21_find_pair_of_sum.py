# Find a pair with given sum in BST
# https://www.geeksforgeeks.org/find-pair-given-sum-bst/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)
    return root


def find_pair_util(root: Node, target: int, unsorted_set: set):
    if root is None:
        return False

    if find_pair_util(root.left, target, unsorted_set):
        return True
    if unsorted_set and (target - root.data) in unsorted_set:
        print("Pair is Found ({},{})".format(target - root.data, root.data))
        return True
    else:
        unsorted_set.add(root.data)

    return find_pair_util(root.right, target, unsorted_set)


def find_pair(root: Node, target: int):
    unsorted_set = set()
    if not find_pair_util(root, target, unsorted_set):
        print("Pair do not exist!")


# Driver code
if __name__ == "__main__":
    root = None
    root = insert(root, 15)
    root = insert(root, 10)
    root = insert(root, 20)
    root = insert(root, 8)
    root = insert(root, 12)
    root = insert(root, 16)
    root = insert(root, 25)
    root = insert(root, 10)
    target = 33
    find_pair(root, target)
