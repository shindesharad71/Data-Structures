# Pairwise swap elements of a given linked list
# https://www.geeksforgeeks.org/pairwise-swap-elements-of-a-given-linked-list/


def pairwise_swap(self):
    temp = self.head

    # There are no nodes in linked list
    if temp is None:
        return

    # Traverse furthur only if there are at least two left
    while temp and temp.next:
        # If both nodes are same,
        # no need to swap data
        if temp.data != temp.next.data:
            # Swap data of node with its next node's data
            temp.data, temp.next.data = temp.next.data, temp.data

        # Move temp by 2 to the next pair
        temp = temp.next.next
