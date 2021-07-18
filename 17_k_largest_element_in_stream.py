# K’th largest element in a stream
# https://www.geeksforgeeks.org/kth-largest-element-in-a-stream/

from heapq import heapify, heappush, heappop, heappushpop
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapify(self.heap)
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        if not self.heap or len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heappushpop(self.heap, val)
        return self.heap[0]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    k = 4

    obj = KthLargest(k, [])

    for i in range(len(arr)):
        largest = obj.add(arr[i])
        print(largest, end=" ")
