# How to check if a given array represents a Binary Heap?
# https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/

# Returns true if arr[i..n-1]
# represents a max-heap
def is_heap(arr: list, i: int, n: int):

    # If a leaf node
    if i >= int((n - 2) / 2):
        return True

    # If an internal node and is greater
    # than its children, and same is
    # recursively true for the children
    if (
        arr[i] >= arr[2 * i + 1]
        and arr[i] >= arr[2 * i + 2]
        and is_heap(arr, 2 * i + 1, n)
        and is_heap(arr, 2 * i + 2, n)
    ):
        return True

    return False


# Driver Code
if __name__ == "__main__":
    arr = [90, 15, 10, 7, 12, 2, 7, 3]
    n = len(arr) - 1

    if is_heap(arr, 0, n):
        print("Yes")
    else:
        print("No")
