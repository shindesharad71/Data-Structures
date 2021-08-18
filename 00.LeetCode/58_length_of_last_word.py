# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])


# Driver Code
if __name__ == "__main__":
    sln = Solution()
    s = "luffy is still joyboy"
    print(sln.lengthOfLastWord(s))
