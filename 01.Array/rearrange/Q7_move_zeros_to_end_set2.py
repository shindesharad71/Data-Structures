# Python3 code to move all zeroes
# at the end of array
# https://www.geeksforgeeks.org/move-zeroes-end-array-set-2-using-single-traversal/


def move_zeros_end_array(arr: list) -> list:
    n = len(arr)
    count = 0  # Count of non-zero elements

    # Traverse the array. If arr[i] is non-zero, then
    # swap the element at index 'count' with the
    # element at index 'i'
    for i in range(0, n):
        if (arr[i] != 0):
            arr[count], arr[i] = arr[i], arr[count]
            count+=1

    return arr


if __name__ == "__main__":
    arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    # expected [1 9 8 4 2 7 6 9 0 0 0 0]
    print(move_zeros_end_array(arr))
