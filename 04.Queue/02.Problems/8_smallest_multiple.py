# Smallest multiple of a given number made of digits 0 and 9 only
# https://www.geeksforgeeks.org/smallest-multiple-of-a-given-number-made-of-digits-0-and-9-only/

from queue import Queue

# Preprocessing function to generate
# all possible numbers formed by 0 and 9
def generate_number():
    global vec

    # Create an empty queue of strings
    q = Queue()

    # enqueue the first number
    q.put("9")

    for count in range(MAX_COUNT, -1, -1):
        s1 = q.queue[0]
        q.get()

        # storing the front of queue
        # in the vector
        vec.append(s1)

        s2 = s1

        # Append "0" to s1 and enqueue it
        s1 += "0"
        q.put(s1)

        # Append "9" to s2 and enqueue it. Note
        # that s2 contains the previous front
        s2 += "9"
        q.put(s2)


def find_multiple(n):
    global vec

    for i in range(len(vec)):
        if int(vec[i]) % n == 0:
            return vec[i]


# Driver Code

# Maximum number of numbers
# made of 0 and 9
MAX_COUNT = 10000

# stack to store all numbers that
# can be formed using digits 0 and
# 9 and are less than 10^5
vec = []
generate_number()
n = 7
print(find_multiple(n))
