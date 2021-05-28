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

    for i in range(n):
        rotation += 1
        if(arr[i] > arr[i+1]):
            break

    return rotation


# Driver code
if __name__ == "__main__":
    arr: list = [7, 9, 11, 12, 15]
    n = len(arr)
    print(f"Rotations required: {count_rotations(arr, n)}")