# Delete a node in a Doubly Linked List
# https://www.geeksforgeeks.org/delete-a-node-in-a-doubly-linked-list/


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

    # Change prev only if node to be deleted is NOT the first node
    if node.prev is not None:
        node.prev.next = node.next
