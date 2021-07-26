# Find elements which are present in first array and not in second
# https://www.geeksforgeeks.org/find-elements-present-first-array-not-second/

# Python3 efficient program to find elements
# which are not present in second array

# Function for finding elements which
# are there in a[] but not in b[].
def findMissing(a, b, n, m):
    # Store all elements of second
    # array in a hash table
    s = dict()
    for i in range(m):
        s[b[i]] = 1

    # Print all elements of first array
    # that are not present in hash table
    for i in range(n):
        if a[i] not in s.keys():
            print(a[i], end=" ")


# Driver code
if __name__ == "__main__":
    a = [1, 2, 6, 3, 4, 5]
    b = [2, 4, 3, 1, 0]
    n = len(a)
    m = len(b)
    findMissing(a, b, n, m)
