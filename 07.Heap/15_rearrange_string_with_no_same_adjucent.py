# Rearrange characters in a string such that no two adjacent are same
# https://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/


def rearrange_string(string: str):
    n = len(string)
    res = ""
    prev = ""

    map = {}

    for i in range(n):
        if string[i] in map:
            map[string[i]] += 1
        else:
            map[string[i]] = 1

    while len(res) < n:
        for val, key in map.items():
            if prev != val and key > 0:
                res = f"{res}{val}"
                map[val] -= 1

    return res


if __name__ == "__main__":
    s = "aaabc"
    print(rearrange_string(s))
