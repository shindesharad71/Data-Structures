# Sort elements by frequency | Set 4 (Efficient approach using hash)
# https://www.geeksforgeeks.org/sort-elements-frequency-set-4-efficient-approach-using-hash/

from collections import defaultdict


def sort_by_freq(arr: list, n: int):
    d = defaultdict(lambda: 0)
    for i in range(n):
        d[arr[i]] += 1

    arr.sort(key=lambda x: (-d[x], x))

    return arr


if __name__ == "__main__":
    arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
    n = len(arr)

    print(sort_by_freq(arr, n))
