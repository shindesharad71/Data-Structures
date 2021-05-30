# Python3 code to move all zeroes
# at the end of array
# https://www.geeksforgeeks.org/move-zeroes-end-array/


def move_zeros_end_array(arr: list) -> list:
    n = len(arr)
    count = 0  # Count of non-zero elements

    # Traverse the array. If element
    # encountered is non-zero, then
    # replace the element at index
    # 'count' with this element
    for i in range(n):
        if arr[i] != 0:

            # here count is incremented
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all
    # elements 0 from count to end.
    while count < n:
        arr[count] = 0
        count += 1

    return arr


if __name__ == "__main__":
    arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    # expected [1 9 8 4 2 7 6 9 0 0 0 0]
    print(move_zeros_end_array(arr))
