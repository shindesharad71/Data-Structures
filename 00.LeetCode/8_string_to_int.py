# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) > 0 and (s[0].isdigit() or s[0] == "-" or s[0] == "+"):
            op = ""
            s = list(s.strip())
            sign = -1 if s[0] == "-" else 1

            if s[0] in ("+", "-"):
                del s[0]

            for i in range(len(s)):
                if s[i].isdigit():
                    op = f"{op}{s[i]}"
                else:
                    break

            if len(op) > 0:
                op = int(op)
                return max(-(2 ** 31), min(sign * op, 2 ** 31 - 1))

        return 0


# Driver code
if __name__ == "__main__":
    # s = "-91283472332"
    s = "    -56"

    sln = Solution()
    print(sln.myAtoi(s))
