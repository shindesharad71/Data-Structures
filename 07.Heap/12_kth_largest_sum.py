# K-th Largest Sum Contiguous Subarray
# https://www.geeksforgeeks.org/k-th-largest-sum-contiguous-subarray/

import heapq


def kth_largest_sum(arr: list, n, k):
    # array to store predix sums
    sum = []
    sum.append(0)
    sum.append(arr[0])
    for i in range(2, n + 1):
        sum.append(sum[i - 1] + arr[i - 1])

    # priority_queue of min heap
    Q = []
    heapq.heapify(Q)

    # loop to calculate the contiguous subarray
    # sum position-wise
    for i in range(1, n + 1):

        # loop to traverse all positions that
        # form contiguous subarray
        for j in range(i, n + 1):
            x = sum[j] - sum[i - 1]

            # if queue has less then k elements,
            # then simply push it
            if len(Q) < k:
                heapq.heappush(Q, x)
            else:
                # it the min heap has equal to
                # k elements then just check
                # if the largest kth element is
                # smaller than x then insert
                # else its of no use
                if Q[0] < x:
                    heapq.heappop(Q)
                    heapq.heappush(Q, x)

    # the top element will be then kth
    # largest element
    return Q[0]


# Driver Code
if __name__ == "__main__":
    a = [10, -10, 20, -40]
    n = len(a)
    k = 6

    # calls the function to find out the
    # k-th largest sum
    print(kth_largest_sum(a, n, k))
