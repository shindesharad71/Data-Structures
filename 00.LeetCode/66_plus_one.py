# 66. Plus One
# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1

        if digits[-1] > 9:
            last_element = digits.pop()
            multiple_digits = str(last_element)
            spt = list(multiple_digits)

            for d in spt:
                digits.append(d)

        return digits


# Driver Code
if __name__ == "__main__":
    sln = Solution()
    digits = [9]
    print(sln.plusOne(digits))
