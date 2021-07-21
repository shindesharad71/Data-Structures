# Find duplicates in a given array when elements are not limited to a range
# https://www.geeksforgeeks.org/find-duplicates-given-array-elements-not-limited-range/


def print_duplicates(arr: list):
    dict = {}

    for ele in arr:
        try:
            dict[ele] += 1
        except:
            dict[ele] = 1

    for item in dict:

        # if frequency is more than 1
        # print the element
        if dict[item] > 1:
            print(item, end=" ")

    print("\n")


# Driver Code
if __name__ == "__main__":
    arr = [12, 11, 40, 12, 5, 6, 5, 12, 11]
    print_duplicates(arr)
