# 66. Plus One
# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = "".join(map(str, digits))
        num = int(num_str) + 1
        num_arr = list(map(int, str(num)))

        return num_arr


# Driver Code
if __name__ == "__main__":
    sln = Solution()
    digits = [9, 9]
    print(sln.plusOne(digits))
