# 1. Two Sum
# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in d:
                return [d[temp], i]
            else:
                d[nums[i]] = i


# Driver Code
if __name__ == "__main__":
    s = Solution()

    arr = [2, 7, 11, 15]
    target = 9

    print(s.twoSum(arr, target))
