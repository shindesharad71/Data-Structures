# Largest Derangement of a Sequence
# https://www.geeksforgeeks.org/largest-derangement-sequence/


def print_largest(seq, N):
    res = [0] * N

    # Insert all elements into a priority queue
    pq = []

    for i in range(N):
        pq.append(seq[i])
