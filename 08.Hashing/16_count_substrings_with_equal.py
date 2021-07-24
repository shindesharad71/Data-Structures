# Count Substrings with equal number of 0s, 1s and 2s
# https://www.geeksforgeeks.org/substring-equal-number-0-1-2/


def get_equal_number(string: str):
    n = len(string)

    map = dict()

    map[(0, 0)] = 1

    zc, oc, tc = 0, 0, 0

    res = 0

    for i in range(n):
        if string[i] == "0":
            zc += 1
        elif string[i] == "1":
            oc += 1
        else:
            tc += 1

        tmp = (zc - oc, zc - tc)

        if tmp not in map:
            res += 0
        else:
            res += map[tmp]

        if tmp in map:
            map[tmp] += 1
        else:
            map[tmp] = 1

    return res


# Driver Code
if __name__ == "__main__":
    string = "0102010"
    print(get_equal_number(string))
