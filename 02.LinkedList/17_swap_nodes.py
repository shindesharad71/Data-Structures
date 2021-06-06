# Swap nodes in a linked list without swapping data
# https://www.geeksforgeeks.org/swap-nodes-in-a-linked-list-without-swapping-data/


def swap_nodes(head_ref, x, y):
    head = head_ref

    # Nothing to do if x and y are same
    if x == y:
        return None

    a = None
    b = None

    # search for x and y in the linked list
    # and store their pointer in a and b
    while head_ref.next:
        if head_ref.next.data == x:
            a = head_ref
        elif head_ref.next.data == y:
            b = head_ref

        head_ref = head_ref.next

    # if we have found both a and b
    # in the linked list swap current
    # pointer and next pointer of these
    if a and b:
        temp = a.next
        a.next = b.next
        b.next = temp
        temp = a.next.next
        a.next.next = b.next.next
        b.next.next = temp

    return head
