# Python3 program to find a
# pair with a given sum in
# a sorted and rotated array
# https://www.geeksforgeeks.org/given-a-sorted-and-rotated-array-find-if-there-is-a-pair-with-a-given-sum/
def pair_in_sorted_rotated(arr: list, x: int):
    length = len(arr)

    for i in range(0, length - 1):
        if arr[i] > arr[i+1]:
            break
    
    # l is now index of smallest element
    l = (i + 1) % length

    # r is now index of largest element
    r = i

    while (l != r):
        # If we find a pair with
        # sum x, we return True
        if (arr[l] + arr[r] == x):
            return True

        # If current pair sum is less,
        # move to the higher sum
        if (arr[l] + arr[r] < x):
            l = (l +1) % length
        else:
            # Move to the lower sum side
            r = (length + r - 1) % length

    return False




if __name__ == "__main__":
    arr = [11, 15, 6, 8, 9, 10]
    x = 16

    # arr = [11, 15, 26, 38, 9, 10]
    # x = 32
    result = pair_in_sorted_rotated(arr, x)
    print(result)