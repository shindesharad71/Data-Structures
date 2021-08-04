# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List
import statistics


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_arr = nums1 + nums2
        final_arr.sort()
        return statistics.median(final_arr)


# Driver Code
if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(s.findMedianSortedArrays(nums1, nums2))
