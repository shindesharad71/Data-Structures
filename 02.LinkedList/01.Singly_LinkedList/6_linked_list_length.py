# Find Length of a Linked List
# https://www.geeksforgeeks.org/find-length-of-a-linked-list-iterative-and-recursive/


def length(self):
    count = 0
    temp = self.head
    while temp:
        count += 1
        temp = temp.next

    print(count)
    return count
