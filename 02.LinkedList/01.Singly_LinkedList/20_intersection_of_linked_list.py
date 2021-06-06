# Intersection of two Sorted Linked Lists
# https://www.geeksforgeeks.org/intersection-of-two-sorted-linked-lists/

""" Link list node """


class Node:
    def __init__(self):
        self.data = 0
        self.next = None


def push(head_ref, new_data):

    """allocate node"""
    new_node = Node()

    """ put in the data  """
    new_node.data = new_data

    """ link the old list off the new node """
    new_node.next = head_ref

    """ move the head to point to the new node """
    (head_ref) = new_node
    return head_ref


"""This solution uses the temporary
dummy to build up the result list """


def sorted_intersect(a, b):
    dummy = Node()
    tail = dummy
    dummy.next = None

    while a != None and b != None:
        if a.data == b.data:
            tail.next = push((tail.next), a.data)
            tail = tail.next
            a = a.next
            b = b.next

        # advance the smaller list
        elif a.data < b.data:
            a = a.next
        else:
            b = b.next
    return dummy.next
