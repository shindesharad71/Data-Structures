# Minimum product of k integers in an array of positive Integers
# https://www.geeksforgeeks.org/minimum-product-k-integers-array-positive-integers/

# Python3 program to find minimum
# product of k elements in an array
import heapq


def min_product(arr, n, k):

    heapq.heapify(arr)
    count = 0
    ans = 1

    # One by one extract
    # items from min heap
    while (arr) and count < k:
        x = heapq.heappop(arr)
        ans = ans * x
        count = count + 1

    return ans


# Driver method
if __name__ == "__main__":
    arr = [198, 76, 544, 123, 154, 675]
    k = 2
    n = len(arr)
    print("Minimum product is ", min_product(arr, n, k))
