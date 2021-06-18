# Sort a stack using recursion
# https://www.geeksforgeeks.org/sort-a-stack-using-recursion/


def sorted_insert(stack, element):
    # Base case: Either stack is empty or newly inserted
    # item is greater than top (more than all existing)
    if len(stack) == 0 or element > stack[-1]:
        stack.append(element)
        return
    else:
        # Remove top item form stack and recur
        temp = stack.pop()
        sorted_insert(stack, element)

        # Put back top item removed earliar
        stack.append(temp)


# Method to sort the stack
def sort_stack(stack):
    # If stack is not empty
    if len(stack) != 0:
        # Remove the top item
        temp = stack.pop()

        # Sort remaining stack
        sort_stack(stack)

        # Push top item back to sorted stack
        sorted_insert(stack, temp)


def print_stack(stack):
    for i in stack[::-1]:
        print(i, end=" ")
    print()


# Driver Code
if __name__ == "__main__":
    stack = []
    stack.append(30)
    stack.append(-5)
    stack.append(18)
    stack.append(14)
    stack.append(3)
    stack.append(10)

    print("Stack elements before sorting: ")
    print_stack(stack)

    sort_stack(stack)

    print("\nStack elements after sorting: ")
    print_stack(stack)
