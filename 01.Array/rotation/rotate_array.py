# Given an array, cyclically rotate the array clockwise by one.
# https://www.geeksforgeeks.org/c-program-cyclically-rotate-array-one/
def rotate_array(arr: list) -> list:
    arr_length = len(arr)
    temp = arr[arr_length - 1]
    for i in range(arr_length - 1, 0, -1): # Reverse
        arr[i] = arr[i - 1]
    arr[0] = temp

    print(arr)
    return arr



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    rotate_array(arr)