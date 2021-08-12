# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = []

        if l1 is None and l2 is None:
            return result

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        current_l1, current_l2 = l1, l2

        while current_l1 or current_l2:
            if current_l1:
                result.append(current_l1.val)
                current_l1 = current_l1.next

            if current_l2:
                result.append(current_l2.val)
                current_l2 = current_l2.next

        sorted_result = result.sort()

        node = None

        for item in sorted_result:
            new_node = ListNode(item)
            if node is None:
                node = new_node

            current = node

            while current:
                current = current.next

            current.next = new_node

        return node
