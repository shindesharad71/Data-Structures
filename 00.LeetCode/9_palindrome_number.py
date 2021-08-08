# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x == int(str(x)[::-1])


# Driver Code
if __name__ == "__main__":
    sln = Solution()
    x = 121
    print(sln.isPalindrome(x))
