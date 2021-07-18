# Sum of all elements between k1’th and k2’th smallest elements
# https://www.geeksforgeeks.org/sum-elements-k1th-k2th-smallest-elements/

# Returns sum between two kth
# smallest element of array
def sumBetweenTwoKth(arr, n, k1, k2):

    # Sort the given array
    arr.sort()

    result = 0
    for i in range(k1, k2 - 1):
        result += arr[i]
    return result


# Driver code
if __name__ == "__main__":
    arr = [20, 8, 22, 4, 12, 10, 14]
    k1 = 3
    k2 = 6
    n = len(arr)
    print(sumBetweenTwoKth(arr, n, k1, k2))
