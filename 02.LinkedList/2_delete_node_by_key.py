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
