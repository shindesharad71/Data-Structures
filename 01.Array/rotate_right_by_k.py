# Python3 program for right rotation of
# an array (Reversal Algorithm)
# https://www.geeksforgeeks.org/reversal-algorithm-right-rotation-array/


def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1


def rotate_right(arr: list, k: int) -> list:
    n = len(arr)
    reverse_array(arr, 0, n - 1)
    reverse_array(arr, 0, k - 1)
    reverse_array(arr, k, n - 1)

    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3  # number of rotations
    print(rotate_right(arr, k))
