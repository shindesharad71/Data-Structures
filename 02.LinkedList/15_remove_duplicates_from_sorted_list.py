# Remove duplicates from a sorted linked list
# https://www.geeksforgeeks.org/remove-duplicates-from-a-sorted-linked-list/


def remove_duplicates(self):
    temp = self.head

    while temp and temp.next:
        if temp.data == temp.next.data:
            new = temp.next.next
            temp.next = None
            temp.next = new
        else:
            temp = temp.next

    return self.head
