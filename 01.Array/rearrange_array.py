# Python3 program for rearrange an
# array such that arr[i] = i.
# https://www.geeksforgeeks.org/rearrange-array-arri/

# Function to rearrange an array
# such that arr[i] = i.
def rearrange_array(arr: list) -> list:
    n = len(arr)
    s = set()

    for i in range(n):
        s.add(arr[i])

    for i in range(n):
        if i in s:
            arr[i] = i
        else:
            arr[i] = -1

    return arr


if __name__ == "__main__":
    arr = [19, 7, 0, 3, 18, 15, 12, 6, 1, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
    print(rearrange_array(arr))
