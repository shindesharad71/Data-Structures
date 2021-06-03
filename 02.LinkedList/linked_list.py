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
        node.next = self.head
        self.head = new_node

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
