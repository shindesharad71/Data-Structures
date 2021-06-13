# How to create mergable stack?
# https://www.geeksforgeeks.org/create-mergable-stack/

# The Node class for Linked List
class Node:
    def __init__(self, data):

        self.next = None
        self.prev = None
        self.data = data


class Stack:

    # Initialize stack class with
    # its head and tail as None
    def __init__(self):

        self.head = None
        self.tail = None

    def push(self, data):

        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.head.next = None
            self.head.prev = None
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):

        if self.head == None:
            print("Stack underflow")

        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            node = self.tail
            self.tail = self.tail.prev
            del node
            self.tail.next = None

    # self (stack) is linked on top (which is tail here) of stack
    # self becomes the merged stack
    def merge(self, stack):
        if stack.head == None:
            return  # if stack is empty self stays as it is
        if self.head == None:  # self (stack) is empty -> point to stack
            self.head = stack.head
            self.tail = stack.tail
            return
        self.head.prev = stack.tail  # link self on top of stack
        stack.tail.nxt = self.head
        self.head = stack.head  # set new head for self (stack)

    def display(self):

        if self.tail != None:
            n = self.tail

            while n != None:
                print(n.data, end=" ")
                n = n.prev

            print()

        else:
            print("Stack Underflow")


# Driver code
ms1 = Stack()
ms2 = Stack()

ms1.push(6)
ms1.push(5)
ms1.push(4)
ms2.push(9)
ms2.push(8)
ms2.push(7)

ms1.merge(ms2)
ms1.display()
while ms1.head != ms1.tail:
    ms1.pop()
print("check pop all elements until head == tail (one element left)")
print("on merged stack: ", end="")
ms1.display()
