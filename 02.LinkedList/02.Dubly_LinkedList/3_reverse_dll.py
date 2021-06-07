# Reverse a Doubly Linked List
# https://www.geeksforgeeks.org/reverse-a-doubly-linked-list/


def reverse(self):
    temp = None
    current = self.head

    # Swap next and prev for all nodes of doubly linked list
    while current:
        temp = current.prev
        current.prev = current.next
        current.next = temp

        current = current.prev

    # Before changing head, check for the cases like
    # empty list and list with only one node
    if temp is not None:
        self.head = temp.prev


"""
method to reverse a Doubly-Linked List using Stacks
"""


def reverse_using_stacks(self):

    stack = []
    temp = self.head
    while temp is not None:
        stack.append(temp.data)
        temp = temp.next

    # Add all the elements in the stack
    # in a sequence to the stack
    temp = self.head
    while temp is not None:
        temp.data = stack.pop()
        temp = temp.next

    # Popped all the elements and the
    # added in the linked list,
    # in a reversed order.
