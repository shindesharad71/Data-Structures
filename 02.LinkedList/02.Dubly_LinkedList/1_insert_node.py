# Insert node in doubly linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# 1. Adding a node at the front of the list
def push(self, data):

    # 1 & 2: Allocate the Node & Put in the data
    new_node = Node(data)

    # 3. Make next of new node as head and previous as NULL
    new_node.next = self.head
    new_node.prev = None

    # 4. change prev of head node to new node
    if self.head is not None:
        self.head.prev = new_node

    # 5. move the head to point to the new node
    self.head = new_node


# 2. Add a node after a given node
def insert_After(self, prev_node, data):

    # 1. check if the given prev_node is NULL
    if prev_node is Node:
        return

    # 2. allocate node  & 3. put in the data
    new_node = Node(data)

    # 4. Make next of new node as next of prev_node
    new_node.next = prev_node.next

    # 5. Make the next of prev_node as new_node
    prev_node.next = new_node

    # 6. Make prev_node as previous of new_node
    new_node.prev = prev_node

    # 7. Change previous of new_node's next node
    if new_node.next is not None:
        new_node.next.prev = new_node
