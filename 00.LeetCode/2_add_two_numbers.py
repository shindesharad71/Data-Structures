# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_num = self.list_to_number(l1)
        second_num = self.list_to_number(l2)

        sum = first_num + second_num

    @staticmethod
    def insert(node: ListNode, val: int) -> ListNode:
        new_node = ListNode(val)
        if node is None:
            return new_node

        current = node
        while current.next:
            current = current.next

        current.next = new_node
        return node

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

    @staticmethod
    def print_list(node: ListNode):
        if node is None:
            return

        current = node
        while current:
            print(current.val, end=" ")
            current = current.next
        print()


# Driver Code
if __name__ == "__main__":
    s = Solution()

    arr1 = [2, 4, 3]
    arr2 = [5, 6, 4]

    l1 = ListNode(arr1[0])
    l2 = ListNode(arr2[0])

    for i in range(1, len(arr1)):
        l1 = s.insert(l1, arr1[i])

    for i in range(1, len(arr2)):
        l2 = s.insert(l2, arr2[i])

    s.print_list(l1)
    s.print_list(l2)
