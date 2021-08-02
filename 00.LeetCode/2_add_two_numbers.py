# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass

    @staticmethod
    def list_to_number(node: ListNode) -> int:
        if not node:
            return 0
        num = "0"
        current = node
        while current:
            num = f"{current.val}{num}"
            current = current.next

        return int(num)


# Driver Code
if __name__ == "__main__":
    s = Solution()
