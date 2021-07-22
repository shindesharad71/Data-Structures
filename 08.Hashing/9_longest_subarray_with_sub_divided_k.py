# Longest subarray with sum divisible by k
# https://www.geeksforgeeks.org/longest-subarray-sum-divisible-k/

# Python3 implementation to find the
# longest subarray with sum divisible by k

# Function to find the longest
# subarray with sum divisible by k
def long_subarr_with_sum_div_by_k(arr: list, n: int, k: int):
    # un-ordered map 'um' implemented as hash table
    um = {}

    # 'mod_arr[i]' stores (sum[0..i] % k)
    mod_arr = [0 for i in range(n)]
    max = 0
    curr_sum = 0

    # Traverse arr[] and build up
    # the array 'mod_arr[]'
    for i in range(n):
        curr_sum += arr[i]

        # As the sum can be negative,
        # taking modulo twice
        mod_arr[i] = ((curr_sum % k) + k) % k

    for i in range(n):

        # If true then sum(0..i) is
        # divisible by k
        if mod_arr[i] == 0:

            # Update 'max'
            max = i + 1

        # If value 'mod_arr[i]' not present in
        # 'um' then store it in 'um' with index
        # of its first occurrence
        elif mod_arr[i] not in um:
            um[mod_arr[i]] = i

        else:

            # If true, then update 'max'
            if max < (i - um[mod_arr[i]]):
                max = i - um[mod_arr[i]]

    # Required length of longest subarray
    # with sum divisible by 'k'
    return max


# Driver Code
if __name__ == "__main__":
    arr = [2, 7, 6, 1, 4, 5]
    n = len(arr)
    k = 3

    print("Length =", long_subarr_with_sum_div_by_k(arr, n, k))
