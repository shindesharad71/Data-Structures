# Queue using list
# https://www.geeksforgeeks.org/queue-in-python/

# Init queue
queue = []

# Adding elements to queue
queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")

print("Initial Queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)
