# Search an element in a Linked List
# https://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive/

# Write a function that searches a given key ‘x’ in a given singly linked list. The function should return true if x is present in linked list and false otherwise.


def search(self, x):
    found = False

    temp = self.head
    while temp:
        if temp.data == x:
            found = True
            break
        temp = temp.next

    return found
