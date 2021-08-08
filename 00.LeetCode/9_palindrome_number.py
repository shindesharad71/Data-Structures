# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        if num_str[0] in ("-", "+"):
            return False

        return x == int(str(x)[::-1])


# Driver Code
if __name__ == "__main__":
    sln = Solution()
    x = -101
    print(sln.isPalindrome(x))
