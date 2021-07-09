# Check if each internal node of a BST has exactly one child
# https://www.geeksforgeeks.org/check-if-each-internal-node-of-a-bst-has-exactly-one-child/


def has_only_ne_child(pre: list, size: int):
    for i in range(size - 1):
        next_diff = pre[i] - pre[i + 1]
        last_diff = pre[i] - pre[size - 1]

        if next_diff * last_diff < 0:
            return False

    return True


# Driver Code
if __name__ == "__main__":

    pre = [8, 3, 5, 7, 6]
    size = len(pre)

    if has_only_ne_child(pre, size):
        print("Yes")
    else:
        print("No")
