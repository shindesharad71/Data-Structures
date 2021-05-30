# Python3 program to rearrange
# positive and negative integers
# in alternate fashion and
# maintaining the order of positive
# and negative numbers
# https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/


def rearrange(arr: list) -> list:
    n = len(arr)

    # sort the array
    arr.sort()

    # initialize two pointers
    # one pointing to the negative number
    # one pointing to the positive number
    i, j = 1, 1

    while j < n:
        if arr[j] > 0:
            break
        j += 1

    # swap the numbers until the given condition gets satisfied
    while (arr[i] < 0) and (j < n):
        # swaping
        arr[i], arr[j] = arr[j], arr[i]

        # increment i by 2
        # because a negative number is followed by a positive number
        i += 2
        j += 1

    return arr


if __name__ == "__main__":
    arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    # expected [-8 1 -2 0 -5 2 4 5 7 8 ]
    print(rearrange(arr))
