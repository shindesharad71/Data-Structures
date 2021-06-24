# Sorting a Queue without extra space
# https://www.geeksforgeeks.org/sorting-queue-without-extra-space/
from queue import Queue


def get_min_index(q: Queue, sorted_index):
    min_index = -1
    min_val = 999999999999
    n = q.qsize()

    for i in range(n):
        current = q.queue[0]
        q.get()

        if current <= min_val and i <= sorted_index:
            min_index = i
            min_val = current

        q.put(current)
    return min_index


def insert_min_to_rear(q: Queue, min_index: int):
    min_val = None
    n = q.qsize()
    for i in range(n):
        current = q.queue[0]
        q.get()
        if i != min_index:
            q.put(current)
        else:
            min_val = current
    q.put(min_val)


def sort_queue(q: Queue):
    for i in range(1, q.qsize() + 1):
        min_index = get_min_index(q, q.qsize() - i)
        insert_min_to_rear(q, min_index)


# Driver code
if __name__ == "__main__":
    q = Queue()
    q.put(30)
    q.put(11)
    q.put(15)
    q.put(4)

    # Sort queue
    sort_queue(q)

    # sorted queue
    while not q.empty():
        print(q.queue[0], end=" ")
        q.get()
    print()
