# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # My Solution
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     first_num = self.list_to_number(l1)
    #     second_num = self.list_to_number(l2)
    #
    #     addition = str(first_num + second_num)
    #
    #     answer_node = None
    #
    #     for n in addition:
    #         answer_node = self.insert(answer_node, int(n))
    #
    #     return answer_node

    # Solution from LeetCode
    # https://leetcode.com/problems/add-two-numbers/discuss/1353295/Python-Runtime-60ms
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = current = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            first_num = l1.val if l1 else 0
            second_num = l2.val if l2 else 0

            carry, val = divmod(first_num + second_num + carry, 10)
            current.next = ListNode(val)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return start.next

    @staticmethod
    def insert(node: ListNode, val: int) -> ListNode:
        new_node = ListNode(val)
        if node is None:
            return new_node

        new_node.next = node
        return new_node

    @staticmethod
    def list_to_number(node: ListNode) -> int:
        if not node:
            return 0
        num = "0"
        current = node
        while current:
            num = f"{num}{current.val}"
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

    list1 = None
    list2 = None

    for i in range(len(arr1)):
        list1 = s.insert(list1, arr1[i])

    for i in range(len(arr2)):
        list2 = s.insert(list2, arr2[i])

    answer = s.addTwoNumbers(list1, list2)

    s.print_list(answer)
