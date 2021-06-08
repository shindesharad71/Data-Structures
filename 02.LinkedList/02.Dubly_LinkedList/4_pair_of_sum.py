# Find pairs with given sum in doubly linked list
# https://www.geeksforgeeks.org/find-pairs-given-sum-doubly-linked-list/


def pair_sum(head, x):
    # set two pointers for start and end of the linked list
    first = head
    second = head

    while second.next:
        second = second.next

    # To tack if we found a pair or not
    found = False

    # The loop terminates when they
    # cross each other (second.next ==
    # first), or they become same
    # (first == second)
    while first != second or second.next != first:
        # If pair found
        if (first.data + second.data) == x:
            found = True
            print("(", first.data, ",", second.data, ")")

            # Move first pointer in forward direction
            first = first.next

            # Move second pointer in backward direction
            second = second.prev
        else:
            if (first.data + second.data) < x:
                first = first.next
            else:
                second = second.prev

    return found
