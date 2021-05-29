# Python program to find minimum element
# in a sorted and rotated array
# https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/
def minimum_elememt(arr: list) -> int:
    n = len(arr)
    low = 0
    high = n - 1

    # We basically find index of minimum element
    
    # EASY METHOD
    # min = arr[0]
    # for i in range(0, n):

    #     if min > arr[i]:

    #         min = arr[i]
    #         min_index = i
    # return min

    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] == arr[high]:
            high -= 1
        elif arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return arr[high]


if __name__ == "__main__":
    arr = [5, 6, 1, 2, 3, 4]
    print(f"Minimun element in given array is - {minimum_elememt(arr)}")
