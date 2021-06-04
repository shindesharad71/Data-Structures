# Delete node by key
# https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def delete_by_key(self, key):
        temp = self.head

        if temp is not None:
            # If key is at stating means at head
            if temp.data == key:
                temp.next = self.head
                temp = None
                return

            # Search for the key to be deleted, keep track of the
            # previous node as we need to change 'prev.next'
            while temp is not None:
                if temp.data == key:
                    break
                prev = temp
                temp = temp.next

            # Key was not present in the list
            if temp == None:
                return

            # Unlink the node
            prev.next = temp.next

            temp = None

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(" %d" % (temp.data)),
            temp = temp.next


if __name__ == "__main__":
    # Driver program
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)

    print("Created Linked List: ")
    llist.printList()
    llist.delete_by_key(1)
    print("\nLinked List after Deletion of 1:")
    llist.printList()
