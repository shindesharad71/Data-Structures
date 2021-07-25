# Print all subarrays with 0 sum
# https://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/


def find_sub_arrays(arr: list, n: int):
    hash_map = {}

    out = []

    total = 0

    for i in range(n):
        total += arr[i]

        if total == 0:
            out.append((0, i))

        al = []

        if total in hash_map:
            al = hash_map.get(total)
            for j in range(len(al)):
                out.append((al[j] + 1, i))
        al.append(i)
        hash_map[total] = al

    return out


def print_output(output):
    for i in output:
        print(f"Subarray found from index {i[0]} to {i[1]}")


# Driver Code
if __name__ == "__main__":
    arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
    n = len(arr)
    out = find_sub_arrays(arr, n)

    # if we did not find any subarray with 0 sum,
    # then subarray does not exists
    if len(out) == 0:
        print("No subarray exists")
    else:
        print_output(out)
