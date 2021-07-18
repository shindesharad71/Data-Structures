# Median in a stream of integers (running integers)
# https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/

from heapq import heappop, heappush, heappushpop


class MedianFinder:
    def __init__(self):
        self.low, self.high = [], []

    def addNum(self, num: int) -> None:
        heappush(self.high, -heappushpop(self.low, -num))
        if len(self.low) < len(self.high):
            heappush(self.low, -heappop(self.high))

    def findMedian(self) -> float:
        return (
            -self.low[0]
            if len(self.low) > len(self.high)
            else (-self.low[0] + self.high[0]) / 2
        )


# Driver Code
if __name__ == "__main__":
    obj = MedianFinder()

    arr = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    print_arr = []
    for i in range(len(arr)):
        obj.addNum(arr[i])
        print_arr.append(arr[i])
        median = obj.findMedian()
        print(f"After reading 1st element of stream - {print_arr} -> median - {median}")
