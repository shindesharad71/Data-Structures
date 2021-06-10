# Write a function to delete a Linked List
# https://www.geeksforgeeks.org/write-a-function-to-delete-a-linked-list/


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

    def delete_list(self):
        # If list is empty
        if self.head is None:
            return

        current = self.head
        while current:
            prev = current.next  # move next node
            # delete the current node
            del current.data
            current = None

            # set current equals prev node
            current = prev

        # In python garbage collection happens therefore, only
        # self.head = None
        # would also delete the link list
        self.head = None  # Just to make it sure!

    def print_list(self):
        temp = self.head

        if temp is None:
            print("List is empty")

        while temp:
            print(temp.data)
            temp = temp.next


# Diver code
if __name__ == "__main__":
    l_list = LinkedList()
    l_list.push(1)
    l_list.push(2)
    l_list.push(3)
    l_list.push(4)
    print("Printing List: ")
    l_list.print_list()

    print("Deleting List: ")
    l_list.delete_list()
    l_list.print_list()
