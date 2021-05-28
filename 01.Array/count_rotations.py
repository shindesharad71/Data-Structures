# Python3 program to find number
# of rotations in a sorted and
# rotated array.
# https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/
#
# Returns count of rotations for
# an array which is first sorted
# in ascending order, then rotated
def count_rotations(arr: list, n: int) -> int:
    rotation = 0

    # We basically find index of minimum element
    min = arr[0]
    for i in range(0, n):

        if min > arr[i]:

            min = arr[i]
            min_index = i

    return min_index


# Driver code
if __name__ == "__main__":
    arr: list = [15, 18, 2, 3, 6, 12]
    n = len(arr)
    print(f"Rotations required: {count_rotations(arr, n)}")
