# Find length of loop in linked list
# https://www.geeksforgeeks.org/find-length-of-loop-in-linked-list/


def loop_length(self):
    # if linked list is empty then there
    # is no loop, so return 0
    if self.head is None:
        return 0

    # Using Floyd’s Cycle-Finding
    # Algorithm/ Slow-Fast Pointer Method
    slow = self.head
    fast = self.head
    flag = 0  # to show that both slow and fast are at start of the Linked List

    while slow and slow.next and fast and fast.next and fast.next.next:
        if slow == fast and flag != 0:
            # Means loop is confirmed in the
            # Linked List. Now slow and fast
            # are both at the same node which
            # is part of the loop
            count = 1
            slow = slow.next
            while slow != fast:
                slow = slow.next
                count += 1
            return count

        slow = slow.next
        fast = fast.next.next
        flag = 1
    return 0  # No loop
