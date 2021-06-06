# Program for nth node from the end of a Linked List
# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/


def nth_node_from_end(self, n):
    temp = self.head

    length = 0

    while temp:
        length += 1
        temp = temp.next

    if n > length:
        print("Location is greater than the length of LinkedList")
        return

    temp = self.head
    for i in range(length - n):
        temp = temp.next
    print(temp.data)
