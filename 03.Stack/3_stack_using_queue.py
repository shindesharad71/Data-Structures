# Implementation using queue module
# Queue module also has a LIFO Queue, which is basically a Stack.
# https://www.geeksforgeeks.org/stack-in-python/

from queue import LifoQueue

# Initializing Stack
stack = LifoQueue(maxsize=4)

# quesize() will show number of element in stack
print(stack.qsize())

# put() will push element in the stack
stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)

print("Full: ", stack.full())
print("Size: ", stack.qsize())

# get() function to pop element from stack in LIFO order
print("Elements popped from the stack")
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get())

print("Empty: ", stack.empty())
