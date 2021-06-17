# Print next greater number of Q queries
# https://www.geeksforgeeks.org/print-next-greater-number-q-queries/

# Python3 program to print
# next greater number
# of Q queries

# array to store the next
# greater element index
def next_greatest(next, a, n):

    # use of stack
    s = []

    # push the 0th
    # index to the stack
    s.append(0)

    # traverse in the
    # loop from 1-nth index
    for i in range(1, n):

        # iterate till loop is empty
        while len(s) != 0:

            # get the topmost
            # index in the stack
            cur = s[-1]

            # if the current element is
            # greater then the top indexth
            # element, then this will be
            # the next greatest index
            # of the top indexth element
            if a[cur] < a[i]:

                # initialise the cur
                # index position's
                # next greatest as index
                next[cur] = i

                # pop the cur index
                # as its greater
                # element has been found
                s.pop()

            # if not greater
            # then break
            else:
                break

        # push the i index so that its
        # next greatest can be found
        s.append(i)

    # iterate for all other
    # index left inside stack
    while len(s) != 0:
        cur = s[-1]

        # mark it as -1 as no
        # element in greater
        # then it in right
        next[cur] = -1
        s.pop()


# answers all
# queries in O(1)
def answer_query(a, next, n, index):

    # stores the next greater
    # element positions
    position = next[index]

    # if position is -1 then no
    # greater element is at right.
    if position == -1:
        return -1

    # if there is a index that
    # has greater element
    # at right then return its
    # value as a[position]
    else:
        return a[position]


# Driver Code
if __name__ == "__main__":

    a = [3, 4, 2, 7, 5, 8, 10, 6]
    n = len(a)

    # initializes the
    # next array as 0
    next = [0 for i in range(n)]

    # calls the function
    # to pre-calculate
    # the next greatest
    # element indexes
    next_greatest(next, a, n)

    # query 1 answered
    print(answer_query(a, next, n, 3), end=" ")

    # query 2 answered
    print(answer_query(a, next, n, 6), end=" ")

    # query 3 answered
    print(answer_query(a, next, n, 1), end=" ")
