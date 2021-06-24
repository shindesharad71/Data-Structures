# Interleave the first half of the queue with second half
# https://www.geeksforgeeks.org/interleave-first-half-queue-second-half/

from queue import Queue


def inter_leave_queue(q: Queue):
    if q.qsize() % 2 != 0:
        print("Input even numbers of integers")

    # Initialise empty stack
    s = []
    half_size = int(q.qsize() / 2)

    # Put first half elements into the stack
    for i in range(half_size):
        s.append(q.queue[0])
        q.get()

    # enqueue back the stack of elements
    while len(s) != 0:
        q.put(s[-1])
        s.pop()

    # dequeue the first half elements of
    # queue and enqueue them back
    # queue: 15 14 13 12 11 16 17 18 19 20
    for i in range(half_size):
        q.put(q.queue[0])
        q.get()

    # Again put the first half elements into
    # the stack queue: 16 17 18 19 20,
    # stack: 11(T) 12 13 14 15
    for i in range(half_size):
        s.append(q.queue[0])
        q.get()

    # interleave the elements of queue and stack
    # queue: 11 16 12 17 13 18 14 19 15 20
    while len(s) != 0:
        q.put(s[-1])
        s.pop()
        q.put(q.queue[0])
        q.get()


# Driver Code
if __name__ == "__main__":
    q = Queue()
    q.put(11)
    q.put(12)
    q.put(13)
    q.put(14)
    q.put(15)
    q.put(16)
    q.put(17)
    q.put(18)
    q.put(19)
    q.put(20)
    inter_leave_queue(q)
    length = q.qsize()
    for i in range(length):
        print(q.queue[0], end=" ")
        q.get()
