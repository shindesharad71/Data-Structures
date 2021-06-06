# Move last element to front of a given Linked List
# https://www.geeksforgeeks.org/move-last-element-to-front-of-a-given-linked-list/


def move_last_to_first(self):
    temp = self.head

    # To check whether we have not received
    # the empty list or list with a single node
    if temp is None or temp.next is None:
        return

    # Iterate till the end to get
    # the last and second last node
    while temp and temp.next:
        second_last_node = temp
        temp = temp.next

    # point the next of the second
    # last node to None
    second_last_node.next = None

    # Make the last node as the first Node
    temp.next = self.head
    self.head = temp
