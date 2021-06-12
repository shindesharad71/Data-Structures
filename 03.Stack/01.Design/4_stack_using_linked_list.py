# Implementation using singly linked list
# https://www.geeksforgeeks.org/stack-in-python/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    # Init stack with dummy node which will get easeier for some operations
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    # String representation of Stack
    def __repr__(self):
        current = self.head.next
        output = ""
        while current:
            output += str(current.data) + "->"
            current = current.next
        return output[:-3]

    # Get the current size of Stack
    def get_size(self):
        return self.size

    # Check of Stack is Empty
    def check_empty(self):
        return self.size == 0

    # Get the top item from Stack
    def peek(self):
        if self.check_empty():
            print("Stack is empty")
        return self.head.next.data

    # Push value into the Stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    # Pop value from Stack
    def pop(self):
        if self.check_empty():
            raise Exception("Stack is empty")

        remove_node = self.head.next
        self.head.next = remove_node.next
        self.size -= 1
        return remove_node.data


# Driver code
if __name__ == "__main__":
    stack = Stack()
    for i in range(11):
        stack.push(i)

    print(f"Stack - {stack}")

    for _ in range(1, 6):
        removed = stack.pop()
        print(f"Pop: {removed}")

    print(f"Stack - {stack}")
