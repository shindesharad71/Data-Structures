# Maximum difference between two subsets of m elements
# https://www.geeksforgeeks.org/difference-maximum-sum-minimum-sum-n-m-elementsin-review/

# Python program to
# find difference
# between max and
# min sum of array


def find_difference(arr: list, n, m):
    max = 0
    min = 0

    # sort array
    arr.sort()
    j = n - 1
    for i in range(m):
        min += arr[i]
        max += arr[j]
        j = j - 1

    return max - min


# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    m = 4

    print(find_difference(arr, n, m))
