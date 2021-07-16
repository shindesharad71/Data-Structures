# Find k numbers with most occurrences in the given array
# https://www.geeksforgeeks.org/find-k-numbers-occurrences-given-array/

import heapq


def print_n_most_frequent(arr: list, n: int, k: int):
    mp = dict()

    for i in range(n):
        if arr[i] not in mp:
            mp[arr[i]] = 0
        else:
            mp[arr[i]] += 1

    heap = [(value, key) for key, value in mp.items()]

    largest = heapq.nlargest(k, heap)

    print(k, " numbers with most " "occurrences are:", sep="")

    # Print the top k elements
    for i in range(k):
        print(largest[i][1], end=" ")


# Driver code
if __name__ == "__main__":
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    n = len(arr)
    k = 2

    print_n_most_frequent(arr, n, k)
