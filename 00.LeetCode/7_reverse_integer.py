# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        if 0 < x < 10:
            return x
        elif x < 0:
            less_than_zero = True
            x = abs(x)
        else:
            less_than_zero = False

        x = str(x)
        reverse_int = ""

        for i in x:
            reverse_int = f"{i}{reverse_int}"

        if less_than_zero:
            reverse_int = -abs(int(reverse_int))
        else:
            reverse_int = int(reverse_int)

        return reverse_int if reverse_int.bit_length() < 32 else 0


# Driver Code
if __name__ == "__main__":
    sln = Solution()
    x = 1534236469  # Very corner case - should return 0
    print(sln.reverse(x))
