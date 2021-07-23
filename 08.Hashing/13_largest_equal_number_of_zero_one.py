# Largest subarray with equal number of 0s and 1s
# https://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/


def max_len(arr: list, n: int):
    hash_map = {}
    curr_sum = 0
    max_length = 0
    ending_index = -1

    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1
        else:
            arr[i] = 1

    for i in range(n):
        curr_sum = curr_sum + arr[i]

        if curr_sum == 0:
            max_length = i + 1
            ending_index = i

        if curr_sum in hash_map:
            if max_length < i - hash_map[curr_sum]:
                max_length = i - hash_map[curr_sum]
                ending_index = i

        else:
            hash_map[curr_sum] = i

    for i in range(n):
        if arr[i] == -1:
            arr[i] = 0
        else:
            arr[i] = 1

    print(ending_index - max_length + 1, end=" ")
    print("to", end=" ")
    print(ending_index)

    return max_length


# Driver Code
if __name__ == "__main__":
    arr = [1, 0, 0, 1, 0, 1, 1]
    n = len(arr)

    max_len(arr, n)
