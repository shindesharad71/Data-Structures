# Write a function to get Nth node in a Linked List
# https://www.geeksforgeeks.org/write-a-function-to-get-nth-node-in-a-linked-list/


def nth_node(self, index):
    count = 0

    temp = self.head

    while temp:
        if count == index:
            return temp.data
        count += 1
        temp = temp.next

    return 0
