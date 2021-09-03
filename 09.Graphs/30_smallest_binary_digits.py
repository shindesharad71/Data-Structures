# Find the smallest binary digit multiple of given number
# https://www.geeksforgeeks.org/find-the-smallest-binary-digit-multiple-of-given-number/


def getMinimumMultipleOfBinaryDigit(A):

    # queue for BFS
    q = []

    # set of visited remainders
    visitedRem = set([])
    t = "1"
    q.append(t)
    while q:
        t = q.pop(0)
        rem = int(t) % A
        if rem == 0:
            return t
        if rem not in visitedRem:
            visitedRem.add(rem)
            q.append(t + "0")
            q.append(t + "1")


# Driver code
if __name__ == "__main__":
    n = 12
    print(getMinimumMultipleOfBinaryDigit(n))
