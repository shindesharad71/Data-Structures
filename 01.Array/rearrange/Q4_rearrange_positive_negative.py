#  Python program to put positive numbers at even indexes (0,  // 2, 4,..) and
#  negative numbers at odd indexes (1, 3, 5, ..)
# https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers-publish/

# The main function that rearranges elements of given array.
# It puts  positive elements at even indexes (0, 2, ..) and
# negative numbers at odd indexes (1, 3, ..).


def rearrange_positive_negative(arr: list) -> list:
    n = len(arr)

    # The following few lines are similar to partition process
    # of QuickSort.  The idea is to consider 0 as pivot and
    # divide the array around it.
    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            # swapping of arr
            arr[i], arr[j] = arr[j], arr[i]

    # Now all positive numbers are at end and negative numbers
    # at the beginning of array. Initialize indexes for starting
    # point of positive and negative numbers to be swapped
    pos, neg = i + 1, 0

    # Increment the negative index by 2 and positive index by 1,
    # i.e., swap every alternate negative number with next
    # positive number
    while pos < n and neg < pos and arr[neg] < 0:

        # swapping of arr
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg += 2

    return arr


if __name__ == "__main__":
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    # expected [4, -3, 5, -1, 6, -7, 2, 8, 9]
    print(rearrange_positive_negative(arr))
