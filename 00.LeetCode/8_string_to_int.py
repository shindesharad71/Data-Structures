# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) > 0 and (s[0].isdigit() or s[0] == "-" or s[0] == "+" or s[0] == " "):
            return s

        return 0


# Driver code
if __name__ == "__main__":
    # s = "words and 987"
    s = "   987"
    sln = Solution()
    print(sln.myAtoi(s))
