# Given an array A[] and a number x, check for pair in A[] with sum as x
# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/


def print_pairs(arr: list, n: int, sum: int):
    s = set()

    for i in range(n):
        temp = sum - arr[i]
        if temp in s:
            print(f"Par with given sum {sum} is ({arr[i]}, {temp})")
            break
        else:
            s.add(arr[i])


# Driver Code
if __name__ == "__main__":
    A = [1, 4, 45, 6, 10, 8]
    sum = 16
    print_pairs(A, len(A), sum)
