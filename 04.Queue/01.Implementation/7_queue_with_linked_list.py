# Queue – Linked List Implementation
# https://www.geeksforgeeks.org/queue-linked-list-implementation/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None


# Driver Code
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
    q.dequeue()
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.dequeue()
    print("Queue Front " + str(q.front.data))
    print("Queue Rear " + str(q.rear.data))
