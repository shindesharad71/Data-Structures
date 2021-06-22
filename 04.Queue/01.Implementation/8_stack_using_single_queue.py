# Implement a stack using single queue
# https://www.geeksforgeeks.org/implement-a-stack-using-single-queue/


class Stack:
    def __init__(self):
        self.arr = []

    def push(self, item):
        size = len(self.arr)
        self.arr.append(item)

        for i in range(size):
            x = self.arr.pop()
            self.arr.append(x)

    def pop(self):
        if len(self.arr) == 0:
            print("Stack underflow")
            return

        x = self.arr.pop()
        return x

    def top(self):
        if len(self.arr) == 0:
            return -1
        return self.arr[-1]

    def is_empty(self):
        return len(self.arr) == 0


if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(20)
    print(f"Top element: {str(s.top())}")
    s.pop()
    s.push(30)
    s.pop()
    print(f"Top element: {str(s.top())}")
