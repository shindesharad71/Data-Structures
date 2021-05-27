# Python program to find maximum value of Sum(i*arr[i])
# returns max possible value of Sum(i*arr[i])
# https://www.geeksforgeeks.org/find-maximum-value-of-sum-iarri-with-only-rotations-on-given-array-allowed/
def max_sum(arr: list):
    arr_sum = 0
    currunt_val = 0
    n = len(arr)

    for i in range(0, n):
        arr_sum = arr_sum + arr[i]
        currunt_val = currunt_val + (i*arr[i])

    max_value = currunt_val

    # try all rotations one by one and find the maximum
    # rotation sum
    for j in range(1, n):
        currunt_val = currunt_val + arr_sum - n * arr[n-j]
        if currunt_val > max_value:
            max_value = currunt_val

    return max_value



if __name__ == "__main__":
    arr: list = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Max sum is: {max_sum(arr)}")