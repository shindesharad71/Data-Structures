# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        MAPPING = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        number, prev = 0, 0
        for char in s[::-1]:
            if MAPPING[char] >= prev:
                number += MAPPING[char]  # sum the value iff previous value same or more
            else:
                number -= MAPPING[
                    char
                ]  # subtract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc

            prev = MAPPING[char]

        return number


# Driver Code
if __name__ == "__main__":
    sln = Solution()
    s = "IX"
    print(sln.romanToInt(s))
