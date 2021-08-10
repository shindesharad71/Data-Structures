# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        OPEN = ("(", "[", "{")
        stack = []

        for char in s:
            if char in OPEN:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                popped = stack.pop()
                if popped == "(" and char == ")":
                    continue
                elif popped == "{" and char == "}":
                    continue
                elif popped == "[" and char == "]":
                    continue
                else:
                    return False

        return len(stack) == 0


# Driver Code
if __name__ == "__main__":
    sln = Solution()
    s = "{[]"
    print(sln.isValid(s))
