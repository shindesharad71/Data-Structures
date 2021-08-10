# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    break
            prefix += strs[0][i]
        return prefix


# Driver Code
if __name__ == "__main__":
    sln = Solution()
    strs = ["flower", "flow", "flight"]
    print(sln.longestCommonPrefix(strs))
