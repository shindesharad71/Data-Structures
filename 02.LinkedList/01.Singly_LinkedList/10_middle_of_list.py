# Find the middle of a given linked list
# https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/


def middle_of_linked_list(self):
    # Initialize two pointers, one will go one step a time (slow), another two at a time (fast)
    slow = self.head
    fast = self.head

    # Iterate till fast's next is null (fast reaches end)
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # return the slow's data, which would be the middle element.
    print("The middle element is ", slow.data)
