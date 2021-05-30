# Python3 program to find
# minimum swaps required
# to club all elements less
# than or equals to k together
# https://www.geeksforgeeks.org/minimum-swaps-required-bring-elements-less-equal-k-together/


def min_swap(arr: list, k: int) -> int:
    n = len(arr)
    count = 0

    # Find count of elements
    # which are less than
    # equals to k
    for i in range(n):
        if arr[i] <= k:
            count += 1

    # Find unwanted elements
    # in current window of
    # size 'count'
    bad = 0
    for i in range(count):
        if arr[i] > k:
            bad = bad + 1

    # Initialize answer with
    # 'bad' value of current
    # window
    ans = bad
    j = count

    for i in range(n):
        if j == n:
            break

        # Decrement count of
        # previous window
        if arr[i] > k:
            bad = bad - 1

        # Increment count of
        # current window
        if arr[j] > k:
            bad = bad + 1

        # Update ans if count
        # of 'bad' is less in
        # current window
        ans = min(ans, bad)

        j = j + 1

    return ans


if __name__ == "__main__":
    arr = [2, 7, 9, 5, 8, 7, 4]
    k = 5
    print(min_swap(arr, k))
