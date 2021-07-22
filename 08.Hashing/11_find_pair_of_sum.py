# Find four elements a, b, c and d in an array such that a+b = c+d
# https://www.geeksforgeeks.org/find-four-elements-a-b-c-and-d-in-an-array-such-that-ab-cd/


def find_pair_of_sum(arr: list, n: int):
    map = {}

    for i in range(n):
        for j in range(i + 1, n):
            sum = arr[i] + arr[j]

            if sum in map:
                print(f"{map[sum]} and ({arr[i]}, {arr[j]})")
                return
            else:
                map[sum] = (arr[i], arr[j])


# Driver code
if __name__ == "__main__":
    arr = [3, 4, 7, 1, 2, 9, 8]
    n = len(arr)
    find_pair_of_sum(arr, n)
