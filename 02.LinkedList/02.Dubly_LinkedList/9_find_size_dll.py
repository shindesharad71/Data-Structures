# Program to find size of Doubly Linked List
# https://www.geeksforgeeks.org/program-find-size-doubly-linked-list/

# This function returns size of linked list
def find_size(node):

    count = 0
    while node != None:
        count = count + 1
        node = node.next

    return count
