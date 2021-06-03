# Linked list practice and implementation
# Node class
class Node:
    def __init__(self, data):
        self.data = data  # Assign Data
        self.next = None  # Initialize next as null


# LinkedList class
class LinkedList:

    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given previous node must be in LinkedList")
            return

        new_node = Node(data)
        new_node.next = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = new_node

    def delete_node(self, key):

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = Node
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp == None:
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None

    # Given a reference to the head of a list
    # and a position, delete the node at a given position
    def delete_node_by_position(self, position):

        # If linked list is empty
        if self.head == None:
            return

        # Store head node
        temp = self.head

        # If head needs to be removed
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

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def delete_list(self):

        # initialize the current node
        current = self.head
        while current:
            prev = current.next  # move next node

            # delete the current node
            del current.data

            # set current equals prev node
            current = prev

        # In python garbage collection happens
        # therefore, only
        # self.head = None
        # would also delete the link list

    # This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.
    def length(self):
        temp = self.head  # Initialise temp
        count = 0  # Initialise count

        # Loop while end of linked list is not reached
        while temp:
            count += 1
            temp = temp.next
        return count

    # This Function checks whether the value
    # x present in the linked list
    def search(self, x):

        # Initialize current to head
        current = self.head

        # loop till current not equal to None
        while current != None:
            if current.data == x:
                return True  # data found

            current = current.next

        return False  # Data Not found

    # Returns data at given index in linked list
    def get_Nth(self, index):
        current = self.head  # Initialise temp
        count = 0  # Index of current node

        # Loop while end of linked list is not reached
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next

        # if we get to this line, the caller was asking
        # for a non-existent element so we assert fail
        assert false
        return 0

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


# Driver Program
if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Link first node with
    #  second
    linked_list.head.next = second
    # Link second node with the third node
    second.next = third

    linked_list.print_list()

    # Insert 6.  So linked list becomes 6->None
    linked_list.append(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    linked_list.push(7)

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    linked_list.push(1)

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    linked_list.append(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    linked_list.insert_after(linked_list.head.next, 8)

    print("Created linked list is:", end=" ")
    linked_list.print_list()

    linked_list.push(7)
    linked_list.push(1)
    linked_list.push(3)
    linked_list.push(2)

    print("Created Linked List: ")
    linked_list.print_list()
    linked_list.delete_node(1)
    print("\nLinked List after Deletion of 1:")
    linked_list.print_list()
