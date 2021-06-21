# Queue using Stacks
# https://www.geeksforgeeks.org/queue-using-stacks/

# enQueue(x)
#   1) Push x to stack1.
#
# deQueue:
#   1) If stack1 is empty then error.
#   2) If stack1 has only one element then return it.
#   3) Recursively pop everything from the stack1, store the popped item
#     in a variable res,  push the res back to stack1 and return res


class Queue:
    def __init__(self):
        self.stack = []

    # Add item to the queue
    def enqueue(self, item):
        self.stack.append(item)

    # Remove item from the queue
    def dequeue(self):
        # Return it queue is empty
        if len(self.stack) == 0:
            print("Queue is empty")
            return

        # Pop an item from the stack
        x = self.stack[-1]
        self.stack.pop()

        # if stack become empty
        # return the popped item
        if len(self.stack) == 0:
            return x

        # Recursive call
        item = self.dequeue()

        # Push popped item back to stack
        self.stack.append(x)

        # Return the result of dequeue() call
        return item


# Driver code
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
