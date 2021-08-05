# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def isPalindrome(self, st: str):
        return st == st[::-1]

    def longestPalindrome(self, s: str) -> str:
        if not s:
            raise Exception("You weren't supposed to be null")

        if self.isPalindrome(s):
            return s

        for i in range(len(s), 0, -1):
            for j in range(0, len(s) - i + 1):
                candidate = s[j : j + i]
                if self.isPalindrome(candidate):
                    return candidate


# Driver Code
if __name__ == "__main__":
    sln = Solution()
    s = "babad"
    print(sln.longestPalindrome(s))
