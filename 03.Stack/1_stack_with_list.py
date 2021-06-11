# Stack
# The functions associated with stack are:

# empty() – Returns whether the stack is empty – Time Complexity : O(1)
# size() – Returns the size of the stack – Time Complexity : O(1)
# top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
# push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
# pop() – Deletes the top most element of the stack – Time Complexity : O(1)

stack = []

# append() function to push element in stack
stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")

print(f"Initial Stack - {stack}")

# pop() function for pop operation on stack
print(f"Element Popped from Stack -")
print(stack.pop())
print(stack.pop())

print(f"Stack after elements are Popped: {stack}")
