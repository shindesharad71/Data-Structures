# Sorting array using Stacks
# https://www.geeksforgeeks.org/sorting-array-using-stacks/

# This function return the sorted stack
def sort_stack(input):
    tmp_stack = []

    while len(input) > 0:
        # pop out the first element
        tmp = input[-1]
        input.pop()

        # while temporary stack is not empty
        # and top of stack is smaller than temp

        while len(tmp_stack) > 0 and tmp_stack[-1] < tmp:
            # pop from temporary stack and
            # append it to the input stack
            input.append(tmp_stack[-1])
            tmp_stack.pop()

        # append temp in temporary of stack
        tmp_stack.append(tmp)

    return tmp_stack


def sort_array_with_stack(arr, n):
    # append array element to stack
    input = []
    i = 0

    while i < n:
        input.append(arr[i])
        i += 1

    # Sort the temprory stack
    tmp_stack = sort_stack(input)
    i = 0

    # Put stack elements in arr[]
    while i < n:
        arr[i] = tmp_stack[-1]
        tmp_stack.pop()
        i = i + 1

    return arr


# Driver code
arr = [10, 5, 15, 45]
n = len(arr)

arr = sort_array_with_stack(arr, n)
i = 0

while i < n:
    print(arr[i], end=" ")
    i = i + 1
print()
