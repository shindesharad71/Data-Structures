# Remove duplicates from an unsorted doubly linked list
# https://www.geeksforgeeks.org/remove-duplicates-unsorted-doubly-linked-list/


def delete_node(self, current):
    head = self.head

    # base case
    if head is None or current is None:
        return

    # If current node is head
    if head == current:
        head = current.next

    # Change next only if node to be deleted is NOT the last node
    if current.next is not None:
        current.next.prev = current.prev

    # Change prev only if node to be is NOT the first node
    if current.prev is not None:
        current.prev.next = current.next

    return head


def remove_duplicates_unsorted(self):
    set = set()
    next = None
    current = self.head

    # traverse up to the end of the list
    while current:
        # if current data is seen before
        if current.data in set:
            # store pointer to the node next to 'current' node
            next = current.next

            # delete the node pointed to by 'current'
            delete_node(current)

            # update 'current'
            current = next
        else:
            # insert the current data in 'set'
            set.add(current.data)

            # move to the next node
            current = current.next
