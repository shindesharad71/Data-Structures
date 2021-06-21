# Array implementation Of Queue
# https://www.geeksforgeeks.org/queue-set-1introduction-and-array-implementation/


class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    def is_full(self) -> bool:
        return self.size == self.capacity

    def is_empty(self) -> bool:
        return self.size == 0

    # Insert item into the queue
    def en_queue(self, item):
        if self.is_full():
            print("Q is Full")
            return

        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size += 1
        print(f"{item} enqueued to queue")

    # Remove item from queue
    def de_queue(self):
        if self.is_empty():
            print("Q is empty")

        print(f"{self.Q[self.front]} dequeued from queue")
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

    def queue_front(self):
        if self.is_empty():
            print("Queue is empty")

        print(f"Front item of the queue is {self.Q[self.front]}")

    def queue_rear(self):
        if self.is_empty():
            print("Queue is empty")

        print(f"Rear item of queue is {self.Q[self.rear]}")


# Driver Code
if __name__ == "__main__":

    queue = Queue(30)
    queue.en_queue(10)
    queue.en_queue(20)
    queue.en_queue(30)
    queue.en_queue(40)
    queue.de_queue()
    queue.queue_front()
    queue.queue_rear()
