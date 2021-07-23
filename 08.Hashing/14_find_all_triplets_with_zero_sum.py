# Find all triplets with zero sum
# https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/


def find_triplets(arr: list, n: int):
    found = False

    for i in range(n - 1):
        s = set()

        for j in range(i + 1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                found = True
            else:
                s.add(arr[j])

    if not found:
        print("No Triplet Found")


# Driver Code
if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    n = len(arr)
    find_triplets(arr, n)
