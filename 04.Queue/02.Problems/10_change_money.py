# Check if X can give change to every person in the Queue
# https://www.geeksforgeeks.org/check-if-x-can-give-change-to-every-person-in-the-queue/

# Given an array of N integers where Ai denotes the currency of note that the i-th person has. The possible
# currencies are 5, 10, and 20. All the N people are standing in a queue waiting to buy an ice cream from X which
# costs Rs 5. Initially, X has an initial balance of 0. Check if X will be able to provide change for all people who
# are waiting to buy ice cream.


def is_changeable(notes, n):
    # To count the 5$ and 10& notes
    five_count = 0
    ten_count = 0

    # Serve the customer in order
    for i in range(n):

        # Increase the number of 5$ note by one
        if notes[i] == 5:
            five_count += 1
        elif notes[i] == 10:

            # decrease the number of note 5$
            # and increase 10$ note by one
            if five_count > 0:
                five_count -= 1
                ten_count += 1
            else:
                return False
        else:
            # decrease 5$ and 10$ note by one
            if five_count > 0 and ten_count > 0:
                five_count -= 1
                ten_count -= 1
            elif five_count >= 3:
                # decrease 5$ note by three
                five_count -= 3
            else:
                return False

    return True


# Driver Code

# queue of customers with available notes.
a = [5, 5, 5, 10, 20]
n = len(a)

# Calling function
if is_changeable(a, n):
    print("YES")
else:
    print("NO")
