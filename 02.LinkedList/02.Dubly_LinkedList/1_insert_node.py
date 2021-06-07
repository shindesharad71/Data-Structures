# Insert node in doubly linked list
# https://www.geeksforgeeks.org/doubly-linked-list/


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


# 3. Add node at the end
def append(self, data):
    # 1. Create Node & 2. Add data
    new_node = Node(data)
    last = self.head

    # 3. This new node is going to be the
    # last node, so make next of it as NULL
    new_node.next = None

    # 4. If the Linked List is empty, then
    #  make the new node as head
    if self.head is None:
        new_node.prev = None
        self.head = new_node
        return

    # 5. Else traverse till the last node
    while last.next:
        last = last.next

    # 6. Change the next of last node
    last.next = new_node

    # 7. Make last node as previous of new node
    new_node.prev = last


# 4. Add a node before a given node
def insert_before(self, next_node, data):
    # 1. Check if given next node is Null
    if next_node is None:
        print("the given next node cannot be NULL")
        return

    # 2. Create node
    new_node = Node(data)

    # 4. Make prev of new node as prev of next_node
    new_node.prev = next_node.prev

    # 5. Make the prev of next_node as new_node
    next_node.prev = new_node

    # 6. Make next_node as next of new_node
    new_node.next = next_node

    # 7. Change next of new_node's previous node
    if new_node.prev != None:
        new_node.prev.next = new_node

    # 8. If the prev of new_node is NULL, it will be the new head node
    else:
        head_ref = new_node

    return head_ref
