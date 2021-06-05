# Remove duplicates from an unsorted linked list
# https://www.geeksforgeeks.org/remove-duplicates-from-an-unsorted-linked-list/


def remove_duplicates(self):

    # Base case of empty list or
    # list with only one element
    if self.head is None or self.head.next is None:
        return

    temp = self.head

    # Hash to store seen values
    hash = set()

    hash.add(temp.data)

    while temp.next:
        if temp.next.data in hash:
            temp.next = temp.next.next
        else:
            hash.add(temp.next.data)
            temp = temp.next

    return self.head
