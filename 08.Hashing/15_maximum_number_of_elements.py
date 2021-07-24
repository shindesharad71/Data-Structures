# Minimum number of distinct elements after removing m items
# https://www.geeksforgeeks.org/minimum-number-of-distinct-elements-after-removing-m-items/


def distinct_ids(arr: list, n: int, mi):
    m = {}
    v = []
    count = 0

    for i in range(n):
        if arr[i] in m:
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1

    # Store into the list value as key and vice-versa
    for i in m:
        v.append([m[i], i])

    v.sort()
    size = len(v)

    for i in range(size):
        if v[i][0] <= mi:
            mi -= v[i][0]
            count += 1

        else:
            return size - count
    return size - count


# Driver code
if __name__ == "__main__":
    arr = [2, 3, 1, 2, 3, 3]
    n = len(arr)

    m = 3

    # To display the result
    print(distinct_ids(arr, n, m))
