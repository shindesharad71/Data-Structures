# A matrix probability question
# https://www.geeksforgeeks.org/a-matrix-probability-question/

# check if (x, y) is valid matrix coordinate
def isSafe(x, y, m, n):
    return 0 <= x < m and 0 <= y < n


# Function to calculate probability
# that after N moves from a given
# position (x, y) in m x n matrix,
# boundaries of the matrix will
# not be crossed.
def findProbability(m, n, x, y, N):
    # boundary crossed
    if not isSafe(x, y, m, n):
        return 0.0

    # N steps taken
    if N == 0:
        return 1.0

    # Initialize result
    prob = 0.0

    # move up
    prob += findProbability(m, n, x - 1, y, N - 1) * 0.25

    # move right
    prob += findProbability(m, n, x, y + 1, N - 1) * 0.25

    # move down
    prob += findProbability(m, n, x + 1, y, N - 1) * 0.25

    # move left
    prob += findProbability(m, n, x, y - 1, N - 1) * 0.25

    return prob


# Driver code
if __name__ == "__main__":
    # matrix size
    m = 5
    n = 5

    # coordinates of starting po
    i = 1
    j = 1

    # Number of steps
    N = 2

    print("Probability is ", findProbability(m, n, i, j, N))
