# Binary Heap
# https://www.geeksforgeeks.org/binary-heap/

# A Python program to demonstrate common binary heap operations

# Import the heap functions from python library
from heapq import heapify, heappop, heappush


# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining heap in varient
# heapify - transform list into heap, in place, in linear time

# A Class for Min Heap
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) / 2

    # Inserts a new key 'k'
    def insert_key(self, k):
        heappush(self.heap, k)

    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decrease_key(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)],
                self.heap[i],
            )

    # Method to remove minimum element from min heap
    def extract_min(self):
        return heappop(self.heap)

    # This function deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()
    def delete_key(self, i):
        self.decrease_key(i, float("-inf"))
        self.extract_min()

    # Get the minimum element from the heap
    def get_min(self):
        self.heap[0]


# Driver Code
if __name__ == "__main__":
    heapObj = MinHeap()
    heapObj.insert_key(3)
    heapObj.insert_key(2)
    heapObj.delete_key(1)
    heapObj.insert_key(15)
    heapObj.insert_key(5)
    heapObj.insert_key(4)
    heapObj.insert_key(45)

    print(heapObj.extract_min())
    print(heapObj.get_min())
    heapObj.decrease_key(2, 1)
    print(heapObj.get_min())
