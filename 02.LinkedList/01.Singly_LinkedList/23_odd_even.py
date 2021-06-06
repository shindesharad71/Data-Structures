# Segregate even and odd nodes in a Linked List
# https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

# Algorithm:
# …1) Get pointer to the last node.
# …2) Move all the odd nodes to the end.
# ……..a) Consider all odd nodes before the first even node and move them to end.
# ……..b) Change the head pointer to point to the first even node.
# ……..b) Consider all odd nodes after the first even node and move them to the end.

# Python program to segregate even and odd nodes in a
# Linked List
head = None  # head of list


def segregate_even_odd():

    global head
    end = head
    prev = None
    curr = head

    # Get pointer to last Node
    while end.next != None:
        end = end.next

    new_end = end

    # Consider all odd nodes before getting first eve node
    while curr.data % 2 != 0 and curr != end:

        new_end.next = curr
        curr = curr.next
        new_end.next.next = None
        new_end = new_end.next

    # do following steps only if there is an even node
    if curr.data % 2 == 0:

        head = curr

        # now curr points to first even node
        while curr != end:

            if curr.data % 2 == 0:

                prev = curr
                curr = curr.next

            else:

                # Break the link between prev and curr
                prev.next = curr.next

                # Make next of curr as None
                curr.next = None

                # Move curr to end
                new_end.next = curr

                # Make curr as new end of list
                new_end = curr

                # Update curr pointer
                curr = prev.next

    # We have to set prev before executing rest of this code
    else:
        prev = curr

    if new_end != end and end.data % 2 != 0:

        prev.next = end.next
        end.next = None
        new_end.next = end
