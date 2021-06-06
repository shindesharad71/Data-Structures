# Quick sort in LinkedList
# https://www.geeksforgeeks.org/quicksort-on-singly-linked-list/

""" takes first and last node,but do not
    break any links in    the whole linked list"""


def partition_last(self, start, end):
    if start == end or start == None or end == None:
        return start

    pivot_prev = start
    curr = start
    pivot = end.data

    """iterate till one before the end,
        no need to iterate till the end because end is pivot"""
    while start != end:
        if start.data < pivot:

            # keep tracks of last modified item
            pivot_prev = curr
            temp = curr.data
            curr.data = start.data
            start.data = temp
            curr = curr.next
        start = start.next

        """swap the position of curr i.e.
        next suitable index and pivot"""
        temp = curr.data
        curr.data = pivot
        end.data = temp

        """return one previous to current because
        current is now pointing to pivot """
        return pivot_prev


def sort(self, start, end):
    if start == None or start == end or start == end.next:
        return

    # spit list and partition recurse
    pivot_prev = self.partition_last(start, end)
    self.sort(start, pivot_prev)

    """
        if pivot is picked and moved to the start,
        that means start and pivot is same
        so pick from next of pivot
    """
    if pivot_prev != None and pivot_prev == start:
        self.sort(pivot_prev.next, end)

    # if pivot is in between of the list,start from next of pivot,
    # since we have pivot_prev, so we move two nodes
    elif pivot_prev != None and pivot_prev.next != None:
        self.sort(pivot_prev.next.next, end)
