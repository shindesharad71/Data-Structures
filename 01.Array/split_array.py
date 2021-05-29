# Python program to split array and move first
# part to end.
# https://www.geeksforgeeks.org/split-array-add-first-part-end/

def split_arr(arr: list, k: int) -> list:
    n = len(arr)
    for i in range(k):
        temp = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        
        arr[n-1] = temp

    return arr

if __name__ == "__main__":
    arr = [12, 10, 5, 6, 52, 36]
    k = 2
    print(split_arr(arr, k))