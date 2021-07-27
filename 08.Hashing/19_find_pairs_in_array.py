# Find pairs in array whose sums already exist in array
# https://www.geeksforgeeks.org/find-pairs-in-array-whose-sums-already-exist-in-array/


def find_pair(arr: list, n: int):
    # hash to store all element of array
    s = {i: 1 for i in arr}

    found = False

    for i in range(n):
        for j in range(i + 1, n):

            if arr[i] in s.keys():
                print(arr[i], arr[j])
                found = True

    if not found:
        print("Not Exists")


# Driver code
if __name__ == "__main__":
    arr = [10, 4, 8, 13, 5]
    n = len(arr)
    find_pair(arr, n)
