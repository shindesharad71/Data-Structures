# Largest Derangement of a Sequence
# https://www.geeksforgeeks.org/largest-derangement-sequence/


def print_largest(seq, N):
    res = [0] * N

    # Insert all elements into a priority queue
    pq = []

    for i in range(N):
        pq.append(seq[i])

    # Fill Up res[] from left to right
    for i in range(N):
        pq.sort(reverse=True)
        d = pq[0]
        del pq[0]

        if d != seq[i] or i == N - 1:
            res[i] = d
        else:
            # New Element popped equals the element
            # in original sequence. Get the next
            # largest element
            res[i] = pq[0]
            del pq[0]
            pq.append(d)

        # If given sequence is in descending order then
        # we need to swap last two elements again
        if res[N - 1] == seq[N - 1]:
            res[N - 1] = res[N - 2]
            res[N - 2] = seq[N - 1]

    print("Largest Derangement")
    for i in range(N):
        print(res[i], end=" ")


# Driver code
if __name__ == "__main__":
    seq = [92, 3, 52, 13, 2, 31, 1]
    n = len(seq)
    print_largest(seq, n)
