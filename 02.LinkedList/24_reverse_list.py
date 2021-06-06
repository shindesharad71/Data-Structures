# Reverse a linked list
# https://www.geeksforgeeks.org/reverse-a-linked-list/

# Using Stack:

# Store the nodes(values and address) in the stack until all the values are entered.
# Once all entries are done, Update the Head pointer to the last location(i.e the last value).
# Start popping the nodes(value and address) and store them in the same order until the stack is empty.
# Update the next pointer of last Node in the stack by NULL.
# Below is the implementation of the above approach:


def reverse(self, head):
    # Initialise the variables
    stack, temp = [], head

    while temp:
        stack.append(temp)
        temp = temp.next

    head = temp = stack.pop()

    # Until stack is not empty
    while len(stack) > 0:
        elem = stack.pop()
        temp.next = elem
        temp = elem

    elem.next = None
    return head
