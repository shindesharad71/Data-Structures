# Swap Kth node from beginning with Kth node from end in a Linked List
# https://www.geeksforgeeks.org/swap-kth-node-from-beginning-with-kth-node-from-end-in-a-linked-list/


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def count_nodes(self):
    count = 0
    temp = self.head
    while temp:
        count += 1
        temp = temp.next

    return count


def swap_nodes(self, k):
    # count all nodes from linked list
    n = count_nodes()

    # Check if K is valid
    if n < k:
        return

    """
    If x (kth node from start) and
    y(kth node from end) are same
    """
    if (2 * k - 1) == n:
        return

    """
    Find the kth node from beginning of linked list.
    We also find previous of kth node because we need
    to update next pointer of the previous.
    """
    x = self.head
    x_prev = Node(None)
    for i in range(k - 1):
        x_prev = x
        x = x.next

    """
    Similarly, find the kth node from end and its
    previous. kth node from end is (n-k + 1)th node
    from beginning
    """
    y = self.head
    y_prev = Node(None)
    for i in range(n - k):
        y_prev = y
        y = y.next

    """
    If x_prev exists, then new next of it will be y.
    Consider the case when y->next is x, in this case,
    x_prev and y are same. So the statement
    "x_prev->next = y" creates a self loop. This self
    loop will be broken when we change y->next.
    """
    if x_prev is not None:
        x_prev.next = y

    # Same thing applies to y_prev
    if y_prev is not None:
        y_prev.next = x

    """
    Swap next pointers of x and y. These statements
    also break self loop if x->next is y or y->next
    is x
    """
    temp = x.next
    x.next = y.next
    y.next = temp

    # Change head pointers when k is 1 or n
    if k == 1:
        self.head = y

    if k == n:
        self.head = x
