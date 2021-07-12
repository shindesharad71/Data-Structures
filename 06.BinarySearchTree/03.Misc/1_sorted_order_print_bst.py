# Sorted order printing of a given array that represents a BST
# https://www.geeksforgeeks.org/sorted-order-printing-of-an-array-that-represents-a-bst/


def print_sorted(arr: list, start: int, end: int):
    if start > end:
        return

    # Print left subtree
    print_sorted(arr, start * 2 + 1, end)

    # Print root
    print(arr[start], end=" ")

    # Print right subtree
    print_sorted(arr, start * 2 + 2, end)


# Driver Code
if __name__ == "__main__":
    arr = [4, 2, 5, 1, 3]
    arr_size = len(arr)
    print_sorted(arr, 0, arr_size - 1)
