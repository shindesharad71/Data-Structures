# Find k numbers with most occurrences in the given array
# https://www.geeksforgeeks.org/find-k-numbers-occurrences-given-array/


def most_frequent(arr: list, n: int, k):
    um = {}
    for i in range(n):
        if arr[i] in um:
            um[arr[i]] += 1
        else:
            um[arr[i]] = 1
    a = [0] * (len(um))
    j = 0
    for i in um:
        a[j] = [i, um[i]]
        j += 1
    a = sorted(a, key=lambda x: x[0], reverse=True)
    a = sorted(a, key=lambda x: x[1], reverse=True)

    # display the top k numbers
    print(k, "numbers with most occurrences are:")
    for i in range(k):
        print(a[i][0], end=" ")


# Driver code
if __name__ == "__main__":
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    n = 8
    k = 2
    most_frequent(arr, n, k)
