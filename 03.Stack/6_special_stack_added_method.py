# Design and Implement Special Stack Data Structure | Added Space Optimized Version
# https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/

# A simple stack class with basic stack functionalities
class stack:
    def __init__(self):

        self.array = []
        self.top = -1
        self.max = 100

    # Stack's member method to check
    # if the stack is empty
    def isEmpty(self):
        return self.top == -1

    # Stack's member method to check
    # if the stack is full
    def isFull(self):
        return self.top == self.max - 1

    # Stack's member method to
    # insert an element to it

    def push(self, data):

        if self.isFull():
            print("Stack OverFlow")
            return
        else:
            self.top += 1
            self.array.append(data)

    # Stack's member method to
    # remove an element from it
    def pop(self):

        if self.isEmpty():
            print("Stack UnderFlow")
            return
        else:
            self.top -= 1
            return self.array.pop()


# A class that supports all the stack
# operations and one additional
# operation getMin() that returns the
# minimum element from stack at
# any time. This class inherits from
# the stack class and uses an
# auxiliary stack that holds
# minimum elements
class SpecialStack(stack):
    def __init__(self):
        super().__init__()
        self.Min = stack()

    # SpecialStack's member method to
    # insert an element to it. This method
    # makes sure that the min stack is also
    # updated with appropriate minimum
    # values
    def push(self, x):

        if self.isEmpty():
            super().push(x)
            self.Min.push(x)
        else:
            super().push(x)
            y = self.Min.pop()
            self.Min.push(y)
            if x <= y:
                self.Min.push(x)
            else:
                self.Min.push(y)

    # SpecialStack's member method to
    # remove an element from it. This
    # method removes top element from
    # min stack also.
    def pop(self):

        x = super().pop()
        self.Min.pop()
        return x

    # SpecialStack's member method
    # to get minimum element from it.
    def getmin(self):

        x = self.Min.pop()
        self.Min.push(x)
        return x


# Driver code
if __name__ == "__main__":

    s = SpecialStack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.getmin())
    s.push(5)
    print(s.getmin())
