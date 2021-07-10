# Check if an array represents Inorder of Binary Search tree or not
# https://www.geeksforgeeks.org/check-array-represents-inorder-binary-search-tree-not/


def is_inorder(arr: list, n: int) -> bool:
    if n == 0 or n == 1:
        return True

    for i in range(1, n):
        # Unsorted pair found
        if arr[i - 1] > arr[i]:
            return False
    # No unsorted pair found
    return True


# Driver code
if __name__ == "__main__":
    arr = [19, 23, 25, 30, 45]
    n = len(arr)

    if is_inorder(arr, n):
        print("Yes")
    else:
        print("No")
