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

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


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
