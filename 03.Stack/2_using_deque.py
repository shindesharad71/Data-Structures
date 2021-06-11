# Stack implementation using dequeue

# Python stack can be implemented using deque class from collections module.
# Deque is preferred over list in the cases where we need quicker append and
# pop operations from both the ends of the container, as deque provides
# an O(1) time complexity for append and pop operations as compared
# to list which provides O(n) time complexity.
# The same methods on deque as seen in list are used, append() and pop().

from collections import deque

stack = deque()

# user append() method to push element in the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(f"Initial Stack - {stack}")

# pop() function to pop element from stack in
# LIFO order
print("Elements popped from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())


print("Stack after elements are popped:")
print(stack)
