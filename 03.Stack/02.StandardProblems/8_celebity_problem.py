# The Celebrity Problem
# https://www.geeksforgeeks.org/the-celebrity-problem/

# Python3 program to find celebrity
# using stack data structure

# Max # of persons in the party
N = 8

# Person with 2 is celebrity
MATRIX = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]


def knows(a, b):
    return MATRIX[a][b]


# Returns -1 if celebrity
# is not present. If present,
# returns id (value from 0 to n-1).
def find_celebrity(n):
    # Handle trivial case of size = 2
    s = []

    for i in range(n):
        s.append(i)

    # Extract top 2
    A = s.pop()
    B = s.pop()

    # Find potential celebrity
    while len(s) > 1:
        if knows(A, B):
            A = s.pop()
        else:
            B = s.pop()

    # If there are only two people and there is no potential candidate
    if len(s) == 0:
        return -1

    # Potential candidate?
    C = s.pop()

    # Last candidate was not
    # examined, it leads one
    # excess comparison (optimize)
    if knows(C, B):
        C = B

    if knows(C, A):
        C = A

    # Check if C is actually
    # a celebrity or not
    for i in range(n):

        # If any person doesn't
        # know 'a' or 'a' doesn't
        # know any person, return -1
        if (i != C) and (knows(C, i) or not (knows(i, C))):
            return -1

    return C


# Driver code
if __name__ == "__main__":

    n = 4
    id_ = find_celebrity(n)

    if id_ == -1:
        print("No celebrity")
    else:
        print("Celebrity ID ", id_)
