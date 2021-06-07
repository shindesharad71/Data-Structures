# Delete a node in a Doubly Linked List


def delete_node(self, node):
    # Base Case
    if self.head is None or node is None:
        return

    # If node to be deleted is head node
    if self.head == node:
        self.head = node.next

    # Change next only if node to be deleted is NOT the last node
    if node.next is not None:
        node.next.prev = node.prev
