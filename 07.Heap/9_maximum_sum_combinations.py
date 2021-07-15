# K maximum sum combinations from two arrays
# https://www.geeksforgeeks.org/k-maximum-sum-combinations-two-arrays/

from queue import PriorityQueue


def k_max_combinations(A, B, N, K):
    pq = PriorityQueue()

    # Insert all the possible
    # combinations in max heap.
    for i in range(N):
        for j in range(N):
            a = A[i] + B[j]
            pq.put((-a, a))

    # Pop first N elements from
    # max heap and display them.
    count = 0
    while count < K:
        print(pq.get()[1])
        count = count + 1


# Driver Code
if __name__ == "__main__":
    A = [4, 2, 5, 1]
    B = [8, 0, 5, 3]
    N = len(A)
    K = 3

    # Function call
    k_max_combinations(A, B, N, K)
