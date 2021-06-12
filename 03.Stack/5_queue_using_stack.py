# Queue using Stacks
# https://www.geeksforgeeks.org/queue-using-stacks/

# Python3 program to implement Queue using
# two stacks with costly enQueue()

# ------------------------------- METHOD 1 ------------------------------
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, item):
        # Move all elements from s1 to s2
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        # Push item into s1
        self.s1.append(item)

        # Push everything back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    # Dequeue an item from the queue
    def deQueue(self):
        if len(self.s1) == 0:
            print("Queue is empty")

        # Return top of s1
        item = self.s1[-1]
        self.s1.pop()
        return item


# ------------------------------- METHOD 2 ------------------------------


class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # EnQueue Item to the Queue
    def enQueue(self, item):
        self.s1.append(item)

    # DeQueue Remove item from the queue
    def deQueue(self):
        # If both stacks are empty
        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Queue is empty")
            return

        # If s2 is empty and s1 has elements
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()

        else:
            return self.s2.pop()


# Driver code
if __name__ == "__main__":
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
