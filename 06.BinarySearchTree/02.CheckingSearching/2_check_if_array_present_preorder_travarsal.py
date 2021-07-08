# Check if a given array can represent Preorder Traversal of Binary Search Tree
# https://www.geeksforgeeks.org/check-if-a-given-array-can-represent-preorder-traversal-of-binary-search-tree/

# Python program for an efficient solution to check if
# a given array can represent Preorder traversal of
# a Binary Search Tree

INT_MIN = -(2 ** 32)


def can_represent_bst(pre: list) -> bool:
    # Create an empty stack
    s = []

    # Init root as minimum possible value
    root = INT_MIN

    # Traverse given array
    for value in pre:
        # If we find a node who is on the right side
        # and smaller than root, return False
        if value < root:
            return False

        # If value(pre[i]) is in right subtree of stack top,
        # Keep removing items smaller than value
        # and make the last removed items as new root
        while len(s) > 0 and s[-1] < value:
            root = s.pop()

        # At this point either stack is empty or value
        # is smaller than root, push value
        s.append(value)

    return True


# Driver Program
if __name__ == "__main__":
    pre1 = [40, 30, 35, 80, 100]
    print(can_represent_bst(pre1))
    pre2 = [40, 30, 35, 20, 80, 100]
    print(can_represent_bst(pre2))
