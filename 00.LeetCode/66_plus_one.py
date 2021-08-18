# 66. Plus One
# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1
        return digits


# Driver Code
if __name__ == "__main__":
    sln = Solution()
    digits = [0]
    print(sln.plusOne(digits))
