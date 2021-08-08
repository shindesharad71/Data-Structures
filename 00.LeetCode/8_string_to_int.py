# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) > 0 and (s[0].isdigit() or s[0] == "-" or s[0] == "+" or s[0] == " "):
            op = ""
            LOWER_BOUND = -2147483648
            UPPER_BOUND = 2147483647

            for c in s:
                if c.isdigit() or c == "-" or c == "+" or c == " ":
                    if c != " ":
                        op = f"{op}{c}"
                else:
                    break

            if len(op) > 0:
                op = int(op)
                if op.bit_length() < 32:
                    return op
                else:
                    return LOWER_BOUND if op < 0 else UPPER_BOUND

        return 0


# Driver code
if __name__ == "__main__":
    # s = "-91283472332"
    # s = "    -+56"

    sln = Solution()
    print(sln.myAtoi(s))
