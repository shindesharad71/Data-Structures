# k largest(or smallest) elements in an array | added Min Heap method
# https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/


def first_k_elements(arr: list, size: int, k: int):
    # Creating Min Heap for given
    # array with only k elements
    # Create min heap with priority queue
    min_heap = []

    for i in range(k):
        min_heap.append(k)

    # Loop For each element in array
    # after the kth element
    for i in range(k, size):
        min_heap.sort()

        # If current element is smaller
        # than minimum ((top element of
        # the minHeap) element, do nothing
        # and continue to next element
        if min_heap[0] > arr[i]:
            continue

        # Otherwise Change minimum element
        # (top element of the minHeap) to
        # current element by polling out
        # the top element of the minHeap
        else:
            min_heap.pop(0)
            min_heap.append(arr[i])

    # Now min heap contains k maximum
    # elements, Iterate and print
    for i in min_heap:
        print(i, end=" ")


# Driver code
if __name__ == "__main__":
    arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
    size = len(arr)

    # Size of Min Heap
    k = 3
    first_k_elements(arr, size, k)
