# Reverse a stack using recursion
# https://www.geeksforgeeks.org/reverse-a-stack-using-recursion/


def create_stack():
    stack = []
    return stack


def is_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)


def pop(stack):
    if is_empty(stack):
        print("Stack Underflow")
        exit(1)

    return stack.pop()


def print_stack(stack):
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i], end=" ")
    print()


def insert_at_bottom(stack, item):
    if is_empty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insert_at_bottom(stack, item)
        push(stack, temp)


def reverse_stack(stack):
    if not is_empty(stack):
        temp = pop(stack)
        reverse_stack(stack)
        insert_at_bottom(stack, temp)


# Driver Code
if __name__ == "__main__":
    stack = create_stack()
    push(stack, 4)
    push(stack, 3)
    push(stack, 2)
    push(stack, 1)

    print("Original Stack -")
    print_stack(stack)

    reverse_stack(stack)

    print("Reversed Stack - ")
    print_stack(stack)
