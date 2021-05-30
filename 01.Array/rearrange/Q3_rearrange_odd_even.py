# Python3 code to rearrange the array
# as per the given condition
# https://www.geeksforgeeks.org/rearrange-array-arri-arrj-even-arri/

def rearrange_odd_even(arr: list) -> list:
    n = len(arr)
    
    # Total even positions
    even_pos = int(n/2)

    odd_pos = n-even_pos

    temp_arr = []
    for i in range(0, n):
        temp_arr.append(arr[i])

    temp_arr.sort()

    j = odd_pos-1

    # fill up odd position in original array
    for i in range(0, n, 2):
        arr[i] = temp_arr[j]
        j = j-1

    j = odd_pos

    # fill up even position in original array
    for i in range(1, n, 2):
        arr[i] = temp_arr[j]
        j = j+1

    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(rearrange_odd_even(arr))