# Delete a Linked List node at a given position
# https://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert node
    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def delete_node_by_position(self, position):
        temp = self.head

        # If list is empty
        if temp == None:
            return

        # If given position is head
        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find previous node of the node to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next.next

        # Unlink the node from linked list
        temp.next = None

        temp.next = next

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


# Driver program to test above function
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)


print("Created Linked List: ")
llist.printList()
llist.delete_node_by_position(4)
print("\nLinked List after Deletion at position 4: ")
llist.printList()
