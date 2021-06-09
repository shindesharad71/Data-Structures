# Insert value in sorted way in a sorted doubly linked list
# https://www.geeksforgeeks.org/insert-value-sorted-way-sorted-doubly-linked-list/


def sorted_insert(self, data):
    new_node = Node(data)

    # If list is empty add it in to the head
    if self.head is None:
        self.head = new_node

    # If the node is to be inserted at the beginning of the doubly linked list
    elif self.head.data >= new_node.data:
        new_node.next = self.head
        new_node.next.prev = new_node
        self.head = new_node
    else:
        current = self.head

        # Locate the node after which the new node  is to be inserted
        while current.next and (current.next.data < new_node.data):
            current = current.next

        # Make appropriate links
        new_node.next = current.next

        # If the new node is not inserted at the end of the list
        if current.next:
            new_node.next.prev = new_node

        current.next = new_node
        new_node.prev = current
