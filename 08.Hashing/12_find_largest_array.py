# Find the length of largest subarray with 0 sum
# https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/


def find_max_len(arr: list):
    max_len = 0

    for i in range(len(arr)):
        curr_sum = 0

        for j in range(i, len(arr)):
            curr_sum += arr[j]

            if curr_sum == 0:
                max_len = max(max_len, j - i + 1)

    return max_len


# Driver Code
if __name__ == "__main__":
    arr = [15, -2, 2, -8, 1, 7, 10, 13]

    print(f"Length of the longest 0 sum subarray is {find_max_len(arr)}")
