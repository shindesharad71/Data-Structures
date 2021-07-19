# Find whether an array is subset of another array
# https://www.geeksforgeeks.org/find-whether-an-array-is-subset-of-another-array-set-1/


def is_subset(arr1, m, arr2, n):
    # Using STL set for hashing
    hashset = set()

    # hset stores all the values of arr1
    for i in range(0, m):
        hashset.add(arr1[i])

    # Loop to check if all elements
    # of arr2 also lies in arr1
    for i in range(0, n):
        if arr2[i] in hashset:
            continue
        else:
            return False

    return True


# Driver Code
if __name__ == "__main__":

    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]

    m = len(arr1)
    n = len(arr2)

    if is_subset(arr1, m, arr2, n):
        print("arr2[] is subset of arr1[] ")
    else:
        print("arr2[] is not a subset of arr1[] ")
