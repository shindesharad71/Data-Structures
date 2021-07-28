# Count pairs whose products exist in array
# https://www.geeksforgeeks.org/count-pairs-whose-products-exist-in-array/


def count_pairs(arr: list, n: int):
    result = 0

    for i in range(n):
        for j in range(i + 1, n):
            product = arr[i] * arr[j]

            for k in range(n):
                if arr[k] == product:
                    result += 1
                    break

    return result


# Driver program
if __name__ == "__main__":
    arr = [6, 2, 4, 12, 5, 3]
    n = len(arr)
    print(count_pairs(arr, n))
