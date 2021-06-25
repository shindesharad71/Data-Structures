# An Interesting Method to Generate Binary Numbers from 1 to n
# https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/

from queue import Queue


def generate_binary_numbers(n):
    q = Queue()

    # Enqueue first binary number
    q.put("1")

    # This loop is like BFS of a tree with 1 as root
    # 0 as left child and 1 as right child and so on
    while n > 0:
        n -= 1
        # Print the front of the queue
        s1 = q.get()
        print(s1)

        # Store s1 before changing it
        s2 = s1

        # Append "0" to s1 and enqueue it
        q.put(s1 + "0")

        # Append "1" to s2 and enqueue it. Note that s2
        # contains the previous front
        q.put(s2 + "1")


# Driver program
n = 10
generate_binary_numbers(n)
