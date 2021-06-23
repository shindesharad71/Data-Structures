# Reversing a Queue
# https://www.geeksforgeeks.org/reversing-a-queue/

from queue import Queue


def reverse_queue(queue: Queue):
    stack = []

    while not queue.empty():
        stack.append(queue.queue[0])
        queue.get()

    while len(stack) != 0:
        queue.put(stack[-1])
        stack.pop()


def print_queue(queue: Queue):
    while not queue.empty():
        print(queue.queue[0], end=" ")
        queue.get()
    print()


# Driver code
if __name__ == "__main__":
    queue = Queue()
    queue.put(10)
    queue.put(20)
    queue.put(30)
    queue.put(40)
    queue.put(50)
    queue.put(60)
    queue.put(70)
    queue.put(80)
    queue.put(90)
    queue.put(100)

    reverse_queue(queue)
    print_queue(queue)
