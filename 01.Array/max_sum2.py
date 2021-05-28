# Given an array arr[] of n integers, find the maximum that maximizes 
# the sum of the value of i*arr[i] where i varies from 0 to n-1.
# https://www.geeksforgeeks.org/maximum-sum-iarri-among-rotations-given-array/

def max_sum(arr: list) -> int:
    max = 0
    n = len(arr)
    for i in range(n):
        currunt_sum = 0
        for j in range(len(arr)):
            currunt_sum = currunt_sum + (j*arr[j])

        if(currunt_sum > max):
            max = currunt_sum
        rotate_by_one(arr, n)
    return max

def rotate_by_one(arr: list, n: int):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp

if __name__ == "__main__":
    arr = [8, 3, 1, 2]
    print(max_sum(arr))