# Delete a Doubly Linked List node at a given position
# https://www.geeksforgeeks.org/delete-doubly-linked-list-node-given-position/


def delete_node(head_ref, current):
    # base case
    if head_ref is None or current is None:
        return

    # If node to be deleted is head node
    if head_ref == current:
        head_ref = current.next

    #  change next node only if node to be deleted is NOT last node
    if current.next is not None:
        current.next.prev = current.prev

    # Change prev only if node to be deleted is NOT the first node
    if current.prev != None:
        current.prev.next = current.next

    return head_ref


def delete_node_by_position(head_ref, n):
    if head_ref is None or n <= 0:
        return

    i = 1
    current = head_ref

    # traverse up to the node at position 'n' from the beginning
    while current and i < n:
        current = current.next
        i += 1

    # if 'n' is greater than the number of nodes in the doubly linked list
    if current is None:
        return

    # delete the node pointed to by 'current'
    delete_node(head_ref, current)

    return head_ref
