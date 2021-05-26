# Python program to rotate an array by d elements
# Function to left rotate arr[] of size n by d
# Problem link - https://www.geeksforgeeks.org/array-rotation/

# Helper method
def rotate_by_one(arr, n) -> None:
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


def rotate_left(arr: list, d: int, n: int) -> None:
    """Function to left rotate arr[] of size n by d

    Args:
        arr (list): Given array
        d (int): By number of elements
        n (int): Size of an array
    """
    # for i in range(d):
    #     rotate_by_one(arr, n)
    print(f"Rotated array - {arr}")


# Driver code
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n = 7
rotate_left(arr, d, n)
