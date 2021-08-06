# 6. ZigZag Conversion


class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        L = [""] * numRows

        index, step = 0, 1

        for x in s:
            L[index] += x
            # @1 start #
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return "".join(L)


# Diver Code
if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3

    sln = Solution()
    print(sln.convert(s, numRows))
