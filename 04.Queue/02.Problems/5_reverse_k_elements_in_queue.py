# Reversing the first K elements of a Queue
# https://www.geeksforgeeks.org/reversing-first-k-elements-queue/

from queue import Queue


def reverse_first_k_elements(k: int, queue: Queue):
    if queue.empty() or k > queue.qsize():
        return

    if k <= 0:
        return

    stack = []

    for i in range(k):
        stack.append(queue.queue[0])
        queue.get()

    while len(stack) != 0:
        queue.put(stack[-1])
        stack.pop()

    for i in range(queue.qsize() - k):
        queue.put(queue.queue[0])
        queue.get()


def print_queue(queue: Queue):
    while not queue.empty():
        print(queue.queue[0])
        queue.get()
    print()


# Driver code
if __name__ == "__main__":
    Queue = Queue()
    Queue.put(10)
    Queue.put(20)
    Queue.put(30)
    Queue.put(40)
    Queue.put(50)
    Queue.put(60)
    Queue.put(70)
    Queue.put(80)
    Queue.put(90)
    Queue.put(100)

    k = 5
    reverse_first_k_elements(k, Queue)
    print_queue(Queue)
