# Given an array arr[] of n integers, find the maximum that maximizes
# the sum of the value of i*arr[i] where i varies from 0 to n-1.
# https://www.geeksforgeeks.org/maximum-sum-iarri-among-rotations-given-array/
def max_sum(arr: list) -> int:
    currunt_sum = 0
    currunt_val = 0
    n = len(arr)

    # Calculate sum of all elements
    for i in range(0, n):
        currunt_sum += arr[i]
        currunt_val += (i * arr[i])

    # Initialize result
    res = currunt_val

    # Compate value for other iterations
    for i in range(1, n - 1):
        # Compute next value using previous
        # value in O(1) time
        next_val = currunt_val - (currunt_sum - arr[i - 1]) + arr[i - 1] * (n - 1)

        # Update current value
        currunt_val = next_val

        # Update result if required
        res = max(res, next_val)

    return res

if __name__ == "__main__":
    arr = [8, 3, 1, 2]
    print(max_sum(arr))
