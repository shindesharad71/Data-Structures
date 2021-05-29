# Iterative python program to reverse an array
# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

def reverse(arr: list) -> list:
    reversed = []
    n = len(arr)

    for i in range(n-1, -1, -1):
        reversed.append(arr[i])

    return reversed
    
    # Short
    # return arr[::-1]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(reverse(arr))