# 67. Add Binary
# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), "b")


# Driver Code
if __name__ == "__main__":
    sln = Solution()
    a = "1010"
    b = "1011"
    print(sln.addBinary(a, b))
