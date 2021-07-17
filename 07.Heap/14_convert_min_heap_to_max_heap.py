# Convert min Heap to max Heap
# https://www.geeksforgeeks.org/convert-min-heap-to-max-heap/


def max_heapify(arr: list, i: int, n: int):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if l < n and arr[l] > arr[i]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, n)


def convert_to_max_heap(arr: list, n: int):
    for i in range(int((n - 2) / 2), -1, -1):
        max_heapify(arr, i, n)


# A utility function to print a
# given array of given size
def print_array(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == "__main__":
    # array representing Min Heap
    arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
    n = len(arr)

    print("Min Heap array : ")
    print_array(arr, n)

    convert_to_max_heap(arr, n)

    print("Max Heap array : ")
    print_array(arr, n)
