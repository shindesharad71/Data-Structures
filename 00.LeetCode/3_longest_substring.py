# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        collection = []
        longest = 0
        for ch in s:

            if ch in collection:
                longest = max(longest, len(collection))
                index = collection.index(ch)
                collection = collection[
                    index + 1 :
                ]  # remove all items before the repeated item including itself

            collection.append(ch)

        return max(longest, len(collection))


# Driver Code
if __name__ == "__main__":
    sln = Solution()
    s = "dvdf"
    print(sln.lengthOfLongestSubstring(s))
