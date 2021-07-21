# Check if a given array contains duplicate elements within k distance from each other
# https://www.geeksforgeeks.org/check-given-array-contains-duplicate-elements-within-k-distance/

# Python 3 program to Check if a given array
# contains duplicate elements within k distance
# from each other
def check_duplicates_within_k(arr: list, n: int, k: int):
    # Creates an empty list
    myset = []

    # Traverse the input array
    for i in range(n):

        # If already present n hash, then we
        # found a duplicate within k distance
        if arr[i] in myset:
            return True

        # Add this item to hashset
        myset.append(arr[i])

        # Remove the k+1 distant item
        if i >= k:
            myset.remove(arr[i - k])
    return False


# Driver Code
if __name__ == "__main__":

    arr = [10, 5, 3, 4, 3, 5, 6]
    n = len(arr)
    if check_duplicates_within_k(arr, n, 3):
        print("Yes")
    else:
        print("No")
