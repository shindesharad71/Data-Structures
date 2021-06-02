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
